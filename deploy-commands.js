import fs from "fs";
import { REST } from "@discordjs/rest";
import { Routes } from "discord-api-types/v9";
import "dotenv/config"; // init .env variables

const clientId = process.env.DISCORD_CLIENTID;
const guildId = process.env.DISCORD_GUILDID;
const token = process.env.DISCORD_TOKEN;

// Build commands
const commands = [];
const commandFiles = fs
  .readdirSync("./commands")
  .filter((file) => file.endsWith(".js"));
for (const file of commandFiles) {
  const command = await import(`./commands/${file}`);
  commands.push(command.data.toJSON());
}
console.log(commands);

// Set commands
const rest = new REST({ version: "9" }).setToken(token);

rest
  .put(Routes.applicationGuildCommands(clientId, guildId), { body: commands })
  .then(() => console.log("Successfully registered application commands."))
  .catch(console.error);

// Make these into global commands
// https://discordjs.guide/interactions/registering-slash-commands.html#global-commands
