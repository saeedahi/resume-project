/**
 * ========================================
 * Animations File
 * ========================================
 */

'use strict';

// ========================================
// Scroll Reveal
// ========================================
document.addEventListener('DOMContentLoaded', function() {
    initScrollReveal();
    initSkillProgressAnimation();
});

// ========================================
// Scroll Reveal
// ========================================
function initScrollReveal() {
    const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
    
    if (revealElements.length === 0) return;
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Add delay for staggered effect
                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, index * 150);
                
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    revealElements.forEach((el, index) => {
        // Add staggered delay via data attribute
        el.style.transitionDelay = (index * 0.1) + 's';
        observer.observe(el);
    });
}

// ========================================
// Skill Progress Animation
// ========================================
function initSkillProgressAnimation() {
    const progressBars = document.querySelectorAll('.skill-progress');
    
    if (progressBars.length === 0) return;
    
    let animated = false;
    
    function animateProgress() {
        if (animated) return;
        
        const triggerPoint = window.innerHeight * 0.8;
        const firstBar = progressBars[0];
        const rect = firstBar.getBoundingClientRect();
        
        if (rect.top < triggerPoint) {
            animated = true;
            
            progressBars.forEach((bar, index) => {
                const targetWidth = bar.style.width;
                bar.style.width = '0%';
                
                setTimeout(() => {
                    bar.style.width = targetWidth;
                }, index * 100);
            });
        }
    }
    
    window.addEventListener('scroll', animateProgress);
    animateProgress();
}

// ========================================
// Parallax Effect (Optional)
// ========================================
function initParallax() {
    const parallaxElements = document.querySelectorAll('.parallax');
    
    if (parallaxElements.length === 0) return;
    
    window.addEventListener('scroll', function() {
        const scrollY = window.pageYOffset;
        
        parallaxElements.forEach(el => {
            const speed = parseFloat(el.getAttribute('data-speed')) || 0.5;
            const yPos = -(scrollY * speed);
            el.style.transform = `translateY(${yPos}px)`;
        });
    });
}

// ========================================
// Mouse Parallax (Hero Visual)
// ========================================
function initMouseParallax() {
    const wrapper = document.querySelector('.profile-wrapper');
    
    if (!wrapper) return;
    
    document.querySelector('.hero-section').addEventListener('mousemove', function(e) {
        const rect = this.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width - 0.5;
        const y = (e.clientY - rect.top) / rect.height - 0.5;
        
        wrapper.style.transform = `rotateX(${y * 5}deg) rotateY(${x * 5}deg)`;
    });
    
    document.querySelector('.hero-section').addEventListener('mouseleave', function() {
        wrapper.style.transform = 'rotateX(0) rotateY(0)';
    });
}

// ========================================
// Intersection Observer for Stats
// ========================================
function initStatsObserver() {
    const statsSection = document.querySelector('.about-stats');
    
    if (!statsSection) return;
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                document.querySelectorAll('.stat-number').forEach(counter => {
                    const target = parseInt(counter.getAttribute('data-count'));
                    animateCounter(counter, target);
                });
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.3 });
    
    observer.observe(statsSection);
}

function animateCounter(element, target) {
    const duration = 2000;
    const startTime = Date.now();
    const startValue = 0;
    
    function update() {
        const elapsed = Date.now() - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        const current = Math.round(eased * target);
        
        element.textContent = current;
        
        if (progress < 1) {
            requestAnimationFrame(update);
        } else {
            element.textContent = target;
        }
    }
    
    update();
}

// ========================================
// Initialize all animations
// ========================================
document.addEventListener('DOMContentLoaded', function() {
    // Mouse parallax is disabled by default for performance
    // Uncomment to enable:
    // initMouseParallax();
    
    // Optional: initParallax();
});