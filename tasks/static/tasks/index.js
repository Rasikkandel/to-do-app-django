
        // Function to toggle strike-through when checkbox is clicked
        function toggleTaskCompletion(checkbox) {
            const taskText = checkbox.nextElementSibling;
            if (checkbox.checked) {
                taskText.classList.add('completed');
            } else {
                taskText.classList.remove('completed');
            }
        }

        // Add event listeners to all checkboxes when page loads
        document.addEventListener('DOMContentLoaded', function() {
            const checkboxes = document.querySelectorAll('.task-checkbox');
            checkboxes.forEach(function(checkbox) {
                checkbox.addEventListener('change', function() {
                    toggleTaskCompletion(this);
                });
            });
        });