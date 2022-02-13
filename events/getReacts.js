import { MessageEmbed } from "discord.js";

import { prefix } from "../data/constants.js";

export const name = "messageCreate";
export const once = false;
export const execute = (client, message) => {
  if (message.author.bot) return;

  const commandBody = message.content.slice(prefix.length);
  const args = commandBody.split(" ");
  const command = args.shift().toLowerCase();

  const record = {};

  if (command === "test") {
    message.channel.messages
      .fetch({ limit: 100 })
      .then((res) => {
        res.forEach((m) => {
          m.reactions.cache.forEach((r) => {
            const key = r.emoji.id
              ? `<:${r.emoji.name}:${r.emoji.id}>`
              : r.emoji.name;
            if (Number.isInteger(record[key]) && record[key] >= 0) {
              record[key] += r.count;
            } else {
              record[key] = r.count;
            }
          });
        });
      })
      .then(() => {
        if (Object.keys(record).length > 0) {
          const sorted = Object.keys(record).sort((a, b) => {
            if (!Number.isInteger(record[a]) || !Number.isInteger(record[b]))
              return 0;
            return record[b] - record[a];
          });
          const embed = new MessageEmbed()
            .setColor("#ffde34")
            .setTitle("Reacts in the last 100 messages")
            .setDescription(
              sorted
                ? sorted.map((k) => `${k}\t ${record[k]}`).join("\n")
                : "Error"
            );
          message.channel.send({ embeds: [embed] });
        }
      });
  }
};
