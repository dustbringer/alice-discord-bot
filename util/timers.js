export const setIntervalAndStart = (fn, t) => {
  fn();
  return setInterval(fn, t);
};
