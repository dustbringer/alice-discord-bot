export const name = "interactionCreate";
export const once = false;
export const execute = async (client, interaction) => {
  if (!interaction.isCommand()) return;

  const command = client.commands.get(interaction.commandName);
  if (!command) return;

  try {
    await command.execute(interaction);
  } catch (error) {
    console.error(error);
    await interaction.reply({
      content: "There was an error while executing this command!",
      ephemeral: true,
    });
  }

  //   const { commandName } = interaction;

  //   if (commandName === "ping") {
  //     await interaction.reply("Pong!");
  //   } else if (commandName === "server") {
  //     await interaction.reply(
  //       `Server name: ${interaction.guild.name}\nTotal members: ${interaction.guild.memberCount}`
  //     );
  //   } else if (commandName === "user") {
  //     await interaction.reply(
  //       `Your tag: ${interaction.user.tag}\nYour id: ${interaction.user.id}`
  //     );
  //   }
};
