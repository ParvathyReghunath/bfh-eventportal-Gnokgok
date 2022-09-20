const btn = document.getElementById('output');

// ✅ Change button text on click
btn.addEventListener('click', function handleClick() {
  const initialText = 'Register';

  btn.innerHTML = `<span style="color: green">Registered<span>`;
});
