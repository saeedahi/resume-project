/**
 * ========================================
 * Main JavaScript File
 * ========================================
 */

'use strict';

// ========================================
// DOM Ready
// ========================================
document.addEventListener('DOMContentLoaded', function() {
    initNavbar();
    initThemeToggle();
    initBackToTop();
    initProgressBar();
    initSmoothScroll();
    initActiveNavLinks();
    // initContactForm();
    initTypingEffect();
    initCounterAnimation();
    initMobileMenu();
});

// ========================================
// Navbar
// ========================================
function initNavbar() {
    const navbar = document.getElementById('navbar');
    let lastScroll = 0;
    
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset || document.documentElement.scrollTop;
        
        if (currentScroll > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        lastScroll = currentScroll;
    });
}

// ========================================
// Theme Toggle
// ========================================
function initThemeToggle() {
    const toggle = document.getElementById('themeToggle');
    const icon = toggle.querySelector('i');
    
    // Check stored theme
    const storedTheme = localStorage.getItem('theme');
    if (storedTheme === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
        icon.className = 'fas fa-sun';
    }
    
    toggle.addEventListener('click', function() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        
        icon.className = newTheme === 'light' ? 'fas fa-sun' : 'fas fa-moon';
    });
}

// ========================================
// Back to Top
// ========================================
function initBackToTop() {
    const btn = document.getElementById('backToTop');
    
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            btn.classList.add('visible');
        } else {
            btn.classList.remove('visible');
        }
    });
    
    btn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// ========================================
// Progress Bar
// ========================================
function initProgressBar() {
    const progressBar = document.getElementById('progress-bar');
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const progress = (scrollTop / scrollHeight) * 100;
        
        progressBar.style.width = progress + '%';
    });
}

// ========================================
// Smooth Scroll
// ========================================
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                
                // Close mobile menu
                const menu = document.getElementById('navbarMenu');
                const hamburger = document.getElementById('hamburger');
                if (menu.classList.contains('open')) {
                    menu.classList.remove('open');
                    hamburger.classList.remove('active');
                }
            }
        });
    });
}

// ========================================
// Active Nav Links
// ========================================
function initActiveNavLinks() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.navbar-menu a');
    
    window.addEventListener('scroll', function() {
        let current = '';
        const scrollPos = window.pageYOffset + 100;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            
            if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + current) {
                link.classList.add('active');
            }
        });
    });
}

// ========================================
// Contact Form
// ========================================
// function initContactForm() {
//     const form = document.getElementById('contactForm');
//
//     form.addEventListener('submit', function(e) {
//         e.preventDefault();
//
//         const name = document.getElementById('name').value.trim();
//         const email = document.getElementById('email').value.trim();
//         const message = document.getElementById('message').value.trim();
//
//         if (!name || !email || !message) {
//             showNotification('لطفاً تمام فیلدها را پر کنید', 'error');
//             return;
//         }
//
//         if (!isValidEmail(email)) {
//             showNotification('لطفاً یک ایمیل معتبر وارد کنید', 'error');
//             return;
//         }
//
//         // Success simulation
//         showNotification('پیام شما با موفقیت ارسال شد!', 'success');
//         form.reset();
//     });
// }

function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

// ========================================
// Notification
// ========================================
function showNotification(message, type = 'success') {
    const existing = document.querySelector('.notification');
    if (existing) {
        existing.remove();
    }
    
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    Object.assign(notification.style, {
        position: 'fixed',
        bottom: '30px',
        left: '50%',
        transform: 'translateX(-50%)',
        padding: '14px 28px',
        borderRadius: '12px',
        backgroundColor: type === 'success' ? '#22C55E' : '#EF4444',
        color: '#fff',
        fontFamily: 'var(--font-family)',
        fontSize: '0.9375rem',
        fontWeight: '500',
        zIndex: '9999',
        boxShadow: '0 8px 30px rgba(0,0,0,0.2)',
        opacity: '0',
        transition: 'opacity 0.3s ease, transform 0.3s ease'
    });
    
    document.body.appendChild(notification);
    
    requestAnimationFrame(() => {
        notification.style.opacity = '1';
        notification.style.transform = 'translateX(-50%) translateY(0)';
    });
    
    setTimeout(() => {
        notification.style.opacity = '0';
        notification.style.transform = 'translateX(-50%) translateY(20px)';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// ========================================
// Typing Effect
// ========================================
function initTypingEffect() {
    const textElement = document.getElementById('typing-text');
    const cursor = document.querySelector('.cursor');
    
    if (!textElement) return;
    
    const texts = [
        'توسعه‌دهنده Backend',
        'Python Developer',
        'Django Developer',
        'API Designer'
    ];
    
    let textIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let isWaiting = false;
    
    function type() {
        const currentText = texts[textIndex];
        
        if (isDeleting) {
            textElement.textContent = currentText.substring(0, charIndex - 1);
            charIndex--;
            
            if (charIndex === 0) {
                isDeleting = false;
                textIndex = (textIndex + 1) % texts.length;
                isWaiting = true;
                setTimeout(() => {
                    isWaiting = false;
                    type();
                }, 500);
                return;
            }
            
            setTimeout(type, 50);
        } else {
            textElement.textContent = currentText.substring(0, charIndex + 1);
            charIndex++;
            
            if (charIndex === currentText.length) {
                isWaiting = true;
                setTimeout(() => {
                    isDeleting = true;
                    isWaiting = false;
                    setTimeout(type, 300);
                }, 2000);
                return;
            }
            
            setTimeout(type, 100);
        }
    }
    
    type();
}

// ========================================
// Counter Animation
// ========================================
function initCounterAnimation() {
    const counters = document.querySelectorAll('.stat-number');
    
    if (counters.length === 0) return;
    
    let animated = false;
    
    function animateCounters() {
        if (animated) return;
        
        const triggerPoint = window.innerHeight * 0.8;
        const firstCounter = counters[0];
        const rect = firstCounter.getBoundingClientRect();
        
        if (rect.top < triggerPoint) {
            animated = true;
            
            counters.forEach(counter => {
                const target = parseInt(counter.getAttribute('data-count'));
                const duration = 2000;
                const startTime = Date.now();
                const startValue = 0;
                
                function updateCounter() {
                    const elapsed = Date.now() - startTime;
                    const progress = Math.min(elapsed / duration, 1);
                    const eased = 1 - Math.pow(1 - progress, 3);
                    const current = Math.round(eased * target);
                    
                    counter.textContent = current;
                    
                    if (progress < 1) {
                        requestAnimationFrame(updateCounter);
                    } else {
                        counter.textContent = target;
                    }
                }
                
                updateCounter();
            });
        }
    }
    
    window.addEventListener('scroll', animateCounters);
    animateCounters();
}

// ========================================
// Mobile Menu
// ========================================
function initMobileMenu() {
    const hamburger = document.getElementById('hamburger');
    const menu = document.getElementById('navbarMenu');
    
    hamburger.addEventListener('click', function() {
        this.classList.toggle('active');
        menu.classList.toggle('open');
    });
    
    // Close on outside click
    document.addEventListener('click', function(e) {
        if (!menu.contains(e.target) && !hamburger.contains(e.target)) {
            menu.classList.remove('open');
            hamburger.classList.remove('active');
        }
    });
}