import { MessageEmbed } from "discord.js";

import { randomChoice } from "../util/arrayUtil.js";

import { prefix } from "../data/constants.js";
import pastaList from "../data/pastaList.js";

export const name = "messageCreate";
export const once = false;
export const execute = (client, message) => {
  if (message.author.bot) return;
  if (!message.content.startsWith(prefix)) return;

  const commandBody = message.content.slice(prefix.length);
  const args = commandBody.split(" ");
  const command = args.shift().toLowerCase();

  if (command === "ping") {
    const timeTaken = Date.now() - message.createdTimestamp;
    message.reply(`Pong! This message had a latency of ${timeTaken}ms.`);
    console.log(`${new Date().toISOString()}; Command: Ping pong`);
  } else if (command === "pasta") {
    let pastaCmd = args.length > 0 ? args[0].toLowerCase() : "random";
    if (pastaCmd === "random") {
      pastaCmd = randomChoice(Object.keys(pastaList));
      console.log(`${new Date().toISOString()}; Command: copypasta random`);
    } else if (Object.keys(pastaList).includes(pastaCmd)) {
      console.log(
        `${new Date().toISOString()}; Command: copypasta '${pastaCmd}'`
      );
    }

    const pasta = pastaList[pastaCmd];
    const pastaEmbed = new MessageEmbed()
      .setTitle(pasta.title)
      .setDescription(pasta.description);
    message.channel.send({ embeds: [pastaEmbed] });
  }
};
