// ============================================
// Engolon CBO - JavaScript Interactivity
// ============================================

document.addEventListener('DOMContentLoaded', function () {
  // Mobile Menu Toggle
  const hamburger = document.querySelector('.hamburger');
  const nav = document.querySelector('nav');

  if (hamburger) {
    hamburger.addEventListener('click', function () {
      hamburger.classList.toggle('active');
      nav.classList.toggle('active');
    });

    // Close menu when a link is clicked
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
      link.addEventListener('click', function () {
        hamburger.classList.remove('active');
        nav.classList.remove('active');
      });
    });
  }

  // Smooth Scroll for Navigation Links
  const scrollLinks = document.querySelectorAll('a[href^="#"]');
  scrollLinks.forEach(link => {
    link.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (href !== '#') {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      }
    });
  });

  // Newsletter Form Validation
  const newsletterForm = document.getElementById('newsletter-form');
  if (newsletterForm) {
    newsletterForm.addEventListener('submit', function (e) {
      e.preventDefault();
      
      const emailInput = document.getElementById('newsletter-email');
      const messageDiv = document.getElementById('form-message');
      const email = emailInput.value.trim();

      // Basic email validation
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      
      if (!emailRegex.test(email)) {
        messageDiv.textContent = 'Please enter a valid email address.';
        messageDiv.classList.remove('success');
        messageDiv.classList.add('error');
        messageDiv.style.display = 'block';
        return;
      }

      // Success message (in real app, send to server)
      messageDiv.textContent = 'Thank you for signing up! Check your email for updates.';
      messageDiv.classList.remove('error');
      messageDiv.classList.add('success');
      messageDiv.style.display = 'block';

      // Clear form
      emailInput.value = '';

      // Hide message after 5 seconds
      setTimeout(function () {
        messageDiv.style.display = 'none';
      }, 5000);
    });
  }

  // Counter Animation for Impact Statistics
  const impactNumbers = document.querySelectorAll('.impact-number');
  
  const animateCounter = (element) => {
    const target = parseInt(element.getAttribute('data-target'), 10);
    const suffix = element.getAttribute('data-suffix') || '';
    let current = 0;
    const increment = Math.ceil(target / 50);
    
    const timer = setInterval(function () {
      current += increment;
      if (current >= target) {
        element.textContent = target.toLocaleString() + suffix;
        clearInterval(timer);
      } else {
        element.textContent = current.toLocaleString() + suffix;
      }
    }, 20);
  };

  // Intersection Observer to trigger animations when section comes into view
  const observerOptions = {
    threshold: 0.5
  };

  const observer = new IntersectionObserver(function (entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        if (entry.target.classList.contains('impact-number')) {
          // Only animate if it hasn't been animated yet
          if (!entry.target.classList.contains('animated')) {
            animateCounter(entry.target);
            entry.target.classList.add('animated');
          }
        }
        // Stop observing this element
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Start observing all impact numbers
  impactNumbers.forEach(number => {
    observer.observe(number);
  });

  // CTA Button Click Handlers (with placeholder actions)
  const donateBtn = document.getElementById('donate-btn');
  const volunteerBtn = document.getElementById('volunteer-btn');
  const resourcesBtn = document.getElementById('resources-btn');
  const contactBtn = document.getElementById('contact-btn');

  if (donateBtn) {
    donateBtn.addEventListener('click', function () {
      console.log('Donate button clicked - redirect to payment page');
      // In production: window.location.href = '/donate';
      alert('Thank you for your interest in donating! Redirecting to donation page...');
    });
  }

  if (volunteerBtn) {
    volunteerBtn.addEventListener('click', function () {
      console.log('Volunteer button clicked - redirect to volunteer form');
      // In production: window.location.href = '/volunteer';
      alert('Thank you for your interest in volunteering! Redirecting to volunteer form...');
    });
  }

  if (resourcesBtn) {
    resourcesBtn.addEventListener('click', function () {
      console.log('Resources button clicked - prepare download');
      // In production: download PDF or redirect to resources page
      alert('Resources will be downloaded. Thank you!');
    });
  }

  if (contactBtn) {
    contactBtn.addEventListener('click', function () {
      console.log('Contact button clicked - redirect to contact page');
      // In production: window.location.href = '/contact';
      alert('Opening contact page...');
    });
  }

  // Scroll to top button (optional enhancement)
  const scrollTopBtn = document.getElementById('scroll-top-btn');
  if (scrollTopBtn) {
    window.addEventListener('scroll', function () {
      if (window.pageYOffset > 300) {
        scrollTopBtn.style.display = 'block';
      } else {
        scrollTopBtn.style.display = 'none';
      }
    });

    scrollTopBtn.addEventListener('click', function () {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  console.log('Engolon CBO website loaded successfully!');
});
