import { randomChoice } from "../util/arrayUtil.js";

import { emotesVege } from "../data/constants.js";

export const name = "messageCreate";
export const once = false;
export const execute = (client, message) => {
  if (message.author.bot) return;

  const msglower = message.content.toLowerCase();
  const emotes = ["💛"]; // emotes to use
  if (msglower.includes("kirito")) {
    console.log(`${new Date().toISOString()}; Reacted to kirito`);
    if (msglower.includes("vege")) {
      console.log(`${new Date().toISOString()}; Reacted to (kirito) vege`);
      emotes.push(randomChoice(emotesVege));
    }

    // Emote in order
    emotes.reduce(
      (prev, curr) => prev.then(() => message.react(curr)),
      Promise.resolve()
    );
  }
};
