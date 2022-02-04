export const name = "error";
export const once = false;
export const execute = (client, event) => {
  console.log(`ERROR: ${event.name}: ${event.message}`);
};
