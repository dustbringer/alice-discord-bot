# alice-discord-bot
Multi-Purpose Discord Bot written for Node.js.

## Local
### Setup
- Create a `.env` file in the root directory of the repository.
  - `DISCORD_CLIENTID`: The bot's client id.
    - Can be found at DiscordDevelopers > OAuth2 > Client Information > Client ID
  - `DISCORD_GUILDID`: The id of the bot's main server
    - Can be found at Discord > Server (right click) > Copy ID
  - `DISCORD_TOKEN`: Token on `Bot` tab in Discord website
  - `DISCORD_GUILD`: Important server name (subject to change)
  - Syntax example
    ```
    DISCORD_TOKEN="token string"
    ```
- Run `npm install` in the root folder

### Run
- Run `npm start` to start the server

## Deployment
Set up the environment variables at the host (e.g. fly.io secrets). If you have set it up locally, make sure the `.env` file is ignored in deployment (e.g. using `.dockerignore` for fly.io).
