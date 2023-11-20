const timer = document.querySelector("#timer");
const actions = document.querySelector("#actions");

const state = {
  INITIAL: 0,
  TIMER_ID: null,
};

const stopTimer = () => {
  clearInterval(state.TIMER_ID);
  state.INITIAL = 0;
  timer.textContent = state.INITIAL;
};

const startTimer = () => {
  stopTimer();
  state.TIMER_ID = setInterval(() => {
    state.INITIAL += 0.1;
    timer.textContent = (state.INITIAL).toFixed(2);
  }, 100);
};

const pauseTimer = () => {
  clearInterval(state.TIMER_ID);
};

actions.addEventListener("click", (e) => {
  if (!(e.target instanceof HTMLButtonElement)) return;

  switch (e.target.textContent) {
    case "Запуск":
      startTimer();
      return;
    case "Пауза":
      pauseTimer();
      return;
    case "Выход из паузы":
      startTimer();
      return;
    case "Остановка":
      stopTimer();
      return;
    default:
      stopTimer();
  }
});
