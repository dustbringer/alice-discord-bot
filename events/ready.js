import { randomChoice } from "../util/arrayUtil.js";
import { setIntervalAndStart } from "../util/timers.js";
import { characters } from "../data/constants.js";

export const name = "ready";
export const once = true;
export const execute = (client) => {
  console.log(`Logged in as ${client.user.tag}!\n`);

  const guilds = client.guilds.cache;
  guilds.forEach((g) => {
    console.log(
      `${client.user.tag} is connected to the following guild:\n`,
      `${g.name}(id: ${g.id})\n`,
      `Guild Size: ${g.memberCount}`
    );
  });

  console.log("");

  // Setting 'Playing' status every hour
  setIntervalAndStart(() => {
    const playing = randomChoice(characters); // choose random element
    client.user.setActivity(`with ${playing}`);
    console.log(`Status updated to 'Playing with ${playing}'\n`);
  }, 3600000);
};
