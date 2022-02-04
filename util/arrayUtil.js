export const randomChoice = (arr) =>
  Array.isArray(arr) &&
  arr.length > 0 &&
  arr[Math.floor(Math.random() * arr.length)];
