// ==========================================
// SHARED AUTHENTICATION JAVASCRIPT
// DRY (Don't Repeat Yourself) - One file for all auth pages
// ==========================================

document.addEventListener('DOMContentLoaded', function() {
    
    // ==========================================
    // PASSWORD TOGGLE FUNCTIONALITY
    // ==========================================
    const togglePassword = document.getElementById('togglePassword');
    const passwordField = document.getElementById('password');
    const eyeIcon = document.getElementById('eyeIcon');
    
    if (togglePassword && passwordField && eyeIcon) {
        togglePassword.addEventListener('click', function() {
            const isPassword = passwordField.type === 'password';
            
            // Toggle input type
            passwordField.type = isPassword ? 'text' : 'password';
            
            // Toggle icon
            if (isPassword) {
                // Eye with slash (hidden password)
                eyeIcon.innerHTML = `
                    <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path>
                    <line x1="1" y1="1" x2="23" y2="23"></line>
                `;
            } else {
                // Normal eye (visible password)
                eyeIcon.innerHTML = `
                    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                    <circle cx="12" cy="12" r="3"></circle>
                `;
            }
        });
    }
    
    // ==========================================
    // FORM VALIDATION & ERROR DISPLAY
    // ==========================================
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const username = document.getElementById('username');
            const password = document.getElementById('password');
            const errorDiv = document.getElementById('error-message');
            
            // Clear previous errors
            if (errorDiv) {
                errorDiv.classList.remove('show');
                errorDiv.textContent = '';
            }
            
            // Basic validation
            let errors = [];
            
            if (username && username.value.trim().length < 3) {
                errors.push('Username must be at least 3 characters long');
            }
            
            if (password && password.value.length < 6) {
                errors.push('Password must be at least 6 characters long');
            }
            
            // Display errors if any
            if (errors.length > 0 && errorDiv) {
                e.preventDefault();
                errorDiv.textContent = errors.join('. ');
                errorDiv.classList.add('show');
                
                // Auto-hide after 5 seconds
                setTimeout(() => {
                    errorDiv.classList.remove('show');
                }, 5000);
            }
        });
    });
    
    // ==========================================
    // SHOW SERVER-SIDE ERRORS (if passed via URL params)
    // ==========================================
    const urlParams = new URLSearchParams(window.location.search);
    const error = urlParams.get('error');
    const success = urlParams.get('success');
    
    if (error) {
        showMessage('error-message', decodeURIComponent(error));
    }
    
    if (success) {
        showMessage('success-message', decodeURIComponent(success));
    }
    
    // ==========================================
    // UTILITY FUNCTION TO SHOW MESSAGES
    // ==========================================
    function showMessage(elementId, message) {
        const messageDiv = document.getElementById(elementId);
        if (messageDiv) {
            messageDiv.textContent = message;
            messageDiv.classList.add('show');
            
            // Auto-hide after 5 seconds
            setTimeout(() => {
                messageDiv.classList.remove('show');
            }, 5000);
        }
    }
});