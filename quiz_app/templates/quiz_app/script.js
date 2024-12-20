const options = document.querySelectorAll('.option input[type="radio"]');

options.forEach(option => {
  option.addEventListener('change', () => {
    document.querySelectorAll('.option').forEach(opt => {
      opt.style.backgroundColor = ''; // Reset all options
    });
    
    if (option.checked) {
      const selectedOption = option.parentElement;
      selectedOption.style.backgroundColor = '#b3e0ff'; // Light up background
    }
  });
});
