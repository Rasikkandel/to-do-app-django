
        // Form submission handling
        document.getElementById('loginForm').addEventListener('submit', function(e) {
            const form = this;
            const submitBtn = form.querySelector('.submit-btn');
            
            // Add loading state
            form.classList.add('loading');
            submitBtn.textContent = 'Signing In...';
            
            // Basic validation
            const username = form.querySelector('input[name="username"]').value.trim();
            const password = form.querySelector('input[name="password"]').value;
            
            if (!username || !password) {
                e.preventDefault();
                form.classList.remove('loading');
                submitBtn.textContent = 'Sign In';
                alert('Please fill in all required fields');
                return;
            }
        });

        // Enhanced input styling
        document.querySelectorAll('input[type="text"], input[type="password"], input[type="email"]').forEach(input => {
            input.addEventListener('input', function() {
                if (this.value.trim() !== '') {
                    this.classList.add('has-value');
                } else {
                    this.classList.remove('has-value');
                }
            });
        });