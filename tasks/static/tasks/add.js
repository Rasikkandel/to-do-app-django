
        function setPriority(value, button) {
            // Update hidden input
            document.getElementById('prio').value = value;
            
            // Update button states
            document.querySelectorAll('.priority-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            button.classList.add('active');
        }
        
        // Form validation
        document.querySelector('form').addEventListener('submit', function(e) {
            const taskInput = document.getElementById('task');
            if (taskInput.value.trim() === '') {
                e.preventDefault();
                alert('Please enter a task description');
                taskInput.focus();
            }
        });