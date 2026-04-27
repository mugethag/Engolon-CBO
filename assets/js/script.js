// ============================================
// Engolon CBO - JavaScript Interactivity
// ============================================

// ============================================
// VOLUNTEER / INTERNSHIP MODAL
// ============================================

function openInvolveModal() {
  document.getElementById('involve-modal').classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeInvolveModal() {
  document.getElementById('involve-modal').classList.remove('active');
  document.body.style.overflow = '';
}

function switchTab(tab) {
  document.getElementById('tab-volunteer').classList.toggle('modal-tab-content--hidden', tab !== 'volunteer');
  document.getElementById('tab-intern').classList.toggle('modal-tab-content--hidden', tab !== 'intern');
  document.querySelectorAll('.modal-tab').forEach(function(btn) {
    btn.classList.toggle('active', btn.textContent.toLowerCase().includes(tab === 'volunteer' ? 'volunteer' : 'intern'));
  });
}

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

  // Newsletter Form Validation
  const newsletterForm = document.getElementById('newsletter-form');
  if (newsletterForm) {
    newsletterForm.addEventListener('submit', function (e) {
      e.preventDefault();
      
      const emailInput = document.getElementById('newsletter-email');
      const messageDiv = document.getElementById('newsletter-form-message');
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

  // CTA Button Click Handlers
  const ctaDonateBtn = document.getElementById('cta-donate-btn');
  const ctaVolunteerBtn = document.getElementById('cta-volunteer-btn');
  const resourcesBtn = document.getElementById('resources-btn');
  const contactBtn = document.getElementById('contact-btn');

  if (ctaDonateBtn) {
    ctaDonateBtn.addEventListener('click', function () {
      window.location.href = 'mailto:info@engolon.com?subject=Donation%20to%20Engolon%20CBO&body=Hello%2C%20I%20would%20like%20to%20make%20a%20donation%20to%20Engolon%20CBO.';
    });
  }

  if (ctaVolunteerBtn) {
    ctaVolunteerBtn.addEventListener('click', function () {
      openInvolveModal();
    });
  }

  if (resourcesBtn) {
    resourcesBtn.addEventListener('click', function () {
      document.getElementById('get-involved').scrollIntoView({ behavior: 'smooth' });
    });
  }

  if (contactBtn) {
    contactBtn.addEventListener('click', function () {
      window.location.href = 'mailto:info@engolon.com?subject=Enquiry%20-%20Engolon%20CBO';
    });
  }

  // ============================================
  // PROGRAM FILTER TABS
  // ============================================

  const filterBtns = document.querySelectorAll('.program-filter-btn');
  const programCards = document.querySelectorAll('.program-card');

  filterBtns.forEach(function(btn) {
    btn.addEventListener('click', function() {
      filterBtns.forEach(function(b) { b.classList.remove('active'); });
      this.classList.add('active');
      const filter = this.dataset.filter;
      programCards.forEach(function(card) {
        if (filter === 'all' || card.dataset.category.includes(filter)) {
          card.classList.remove('hidden');
        } else {
          card.classList.add('hidden');
        }
      });
    });
  });

  // ============================================
  // TOUR BOOKING CALENDAR & FORM
  // ============================================
  
  const tourDateInput = document.getElementById('tour-date');
  const calendarPicker = document.getElementById('calendar-picker');
  let currentMonth = new Date().getMonth();
  let currentYear = new Date().getFullYear();
  let selectedDate = null;

  // Function to render calendar
  function renderCalendar() {
    calendarPicker.innerHTML = '';
    
    const monthNames = ['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December'];
    const dayNames = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    
    // Header with navigation
    const header = document.createElement('div');
    header.className = 'calendar-header';
    
    const prevBtn = document.createElement('button');
    prevBtn.innerHTML = '←';
    prevBtn.type = 'button';
    prevBtn.addEventListener('click', (e) => {
      e.preventDefault();
      if (currentMonth === 0) {
        currentMonth = 11;
        currentYear--;
      } else {
        currentMonth--;
      }
      renderCalendar();
    });
    
    const monthYear = document.createElement('h3');
    monthYear.textContent = monthNames[currentMonth] + ' ' + currentYear;
    
    const nextBtn = document.createElement('button');
    nextBtn.innerHTML = '→';
    nextBtn.type = 'button';
    nextBtn.addEventListener('click', (e) => {
      e.preventDefault();
      if (currentMonth === 11) {
        currentMonth = 0;
        currentYear++;
      } else {
        currentMonth++;
      }
      renderCalendar();
    });
    
    header.appendChild(prevBtn);
    header.appendChild(monthYear);
    header.appendChild(nextBtn);
    calendarPicker.appendChild(header);
    
    // Weekday headers
    const weekdaysDiv = document.createElement('div');
    weekdaysDiv.className = 'calendar-weekdays';
    dayNames.forEach(day => {
      const span = document.createElement('span');
      span.textContent = day;
      weekdaysDiv.appendChild(span);
    });
    calendarPicker.appendChild(weekdaysDiv);
    
    // Days
    const daysDiv = document.createElement('div');
    daysDiv.className = 'calendar-days';
    
    const firstDay = new Date(currentYear, currentMonth, 1).getDay();
    const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
    const today = new Date();
    
    // Previous month's days
    const prevMonthDays = new Date(currentYear, currentMonth, 0).getDate();
    for (let i = firstDay - 1; i >= 0; i--) {
      const dayDiv = document.createElement('div');
      dayDiv.className = 'calendar-day other-month';
      dayDiv.textContent = prevMonthDays - i;
      daysDiv.appendChild(dayDiv);
    }
    
    // Current month's days
    for (let day = 1; day <= daysInMonth; day++) {
      const dayDiv = document.createElement('div');
      dayDiv.className = 'calendar-day';
      dayDiv.textContent = day;
      
      const dateObj = new Date(currentYear, currentMonth, day);
      
      // Disable past dates and Sundays (for example)
      if (dateObj < today || dateObj.getDay() === 0) {
        dayDiv.classList.add('disabled');
      } else {
        dayDiv.addEventListener('click', (e) => {
          e.preventDefault();
          selectDate(dateObj);
        });
      }
      
      // Highlight selected date
      if (selectedDate && 
          dateObj.getDate() === selectedDate.getDate() &&
          dateObj.getMonth() === selectedDate.getMonth() &&
          dateObj.getFullYear() === selectedDate.getFullYear()) {
        dayDiv.classList.add('selected');
      }
      
      daysDiv.appendChild(dayDiv);
    }
    
    // Next month's days
    const totalCells = daysDiv.children.length;
    const remainingCells = 42 - totalCells; // 6 weeks * 7 days
    for (let day = 1; day <= remainingCells; day++) {
      const dayDiv = document.createElement('div');
      dayDiv.className = 'calendar-day other-month';
      dayDiv.textContent = day;
      daysDiv.appendChild(dayDiv);
    }
    
    calendarPicker.appendChild(daysDiv);
  }

  function selectDate(dateObj) {
    selectedDate = dateObj;
    const dateString = dateObj.toLocaleDateString('en-US', {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
    tourDateInput.value = dateString;
    calendarPicker.classList.remove('active');
    renderCalendar();
  }

  // Toggle calendar on input click
  if (tourDateInput) {
    tourDateInput.addEventListener('click', (e) => {
      e.preventDefault();
      calendarPicker.classList.toggle('active');
      if (calendarPicker.classList.contains('active')) {
        renderCalendar();
      }
    });
  }

  // Close calendar when clicking outside
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.date-picker-wrapper')) {
      calendarPicker.classList.remove('active');
    }
  });

  // ============================================
  // TOUR BOOKING FORM SUBMISSION
  // ============================================
  
  const tourBookingForm = document.getElementById('tour-booking-form');
  if (tourBookingForm) {
    tourBookingForm.addEventListener('submit', function (e) {
      e.preventDefault();
      
      const formData = {
        name: document.getElementById('visitor-name').value,
        email: document.getElementById('visitor-email').value,
        phone: document.getElementById('visitor-phone').value,
        groupSize: document.getElementById('group-size').value,
        tourType: document.getElementById('tour-select').value,
        date: document.getElementById('tour-date').value,
        interests: document.getElementById('interests').value,
        terms: document.querySelector('input[name="terms"]').checked
      };

      // Validation
      if (!formData.name || !formData.email || !formData.phone || !formData.groupSize || 
          !formData.tourType || !formData.date || !formData.terms) {
        showFormMessage('Please fill in all required fields and agree to the terms.', 'error');
        return;
      }

      // Email validation
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(formData.email)) {
        showFormMessage('Please enter a valid email address.', 'error');
        return;
      }

      // In production, send to server/email service
      console.log('Tour Booking Data:', formData);
      
      // Success message
      showFormMessage('Thank you for your booking request! We\'ll confirm your tour within 24 hours.', 'success');
      
      // Reset form
      tourBookingForm.reset();
      tourDateInput.value = '';
      selectedDate = null;
      
      // Scroll to message
      document.querySelector('.form-message').scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
  }

  // ============================================
  // MODAL INVOLVE FORM SUBMISSION
  // ============================================

  const modalInvolveForm = document.getElementById('modal-involve-form');
  if (modalInvolveForm) {
    modalInvolveForm.addEventListener('submit', function(e) {
      e.preventDefault();
      const name = document.getElementById('m-name').value.trim();
      const email = document.getElementById('m-email').value.trim();
      const type = document.getElementById('m-type').value;
      const area = document.getElementById('m-area').value;
      const availability = document.getElementById('m-availability').value;
      const msgDiv = document.getElementById('modal-form-msg');
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

      if (!name || !email || !type || !area || !availability) {
        msgDiv.textContent = 'Please fill in all required fields.';
        msgDiv.className = 'form-message error';
        return;
      }
      if (!emailRegex.test(email)) {
        msgDiv.textContent = 'Please enter a valid email address.';
        msgDiv.className = 'form-message error';
        return;
      }

      console.log('Modal involve form:', { name, email, type, area, availability });
      msgDiv.textContent = 'Thank you! We\'ll be in touch within 3 business days.';
      msgDiv.className = 'form-message success';
      modalInvolveForm.reset();

      setTimeout(function() {
        closeInvolveModal();
        msgDiv.className = 'form-message modal-form-msg--hidden';
      }, 3000);
    });
  }

  // ============================================
  // GET INVOLVED FORM SUBMISSION
  // ============================================

  const involveForm = document.getElementById('involve-form');
  if (involveForm) {
    involveForm.addEventListener('submit', function (e) {
      e.preventDefault();

      const name = document.getElementById('involve-name').value.trim();
      const email = document.getElementById('involve-email').value.trim();
      const type = document.getElementById('involve-type').value;
      const area = document.getElementById('involve-area').value;
      const availability = document.getElementById('involve-availability').value;
      const messageDiv = document.getElementById('involve-form-message');

      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

      if (!name || !email || !type || !area || !availability) {
        messageDiv.textContent = 'Please fill in all required fields.';
        messageDiv.classList.remove('success');
        messageDiv.classList.add('error');
        messageDiv.style.display = 'block';
        return;
      }

      if (!emailRegex.test(email)) {
        messageDiv.textContent = 'Please enter a valid email address.';
        messageDiv.classList.remove('success');
        messageDiv.classList.add('error');
        messageDiv.style.display = 'block';
        return;
      }

      // In production, submit to a backend / email service
      console.log('Get Involved submission:', { name, email, type, area, availability });

      messageDiv.textContent = 'Thank you! We have received your interest and will be in touch within 3 business days.';
      messageDiv.classList.remove('error');
      messageDiv.classList.add('success');
      messageDiv.style.display = 'block';

      involveForm.reset();

      messageDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });

      setTimeout(() => {
        messageDiv.style.display = 'none';
      }, 8000);
    });
  }

  function showFormMessage(message, type) {
    const messageDiv = document.getElementById('form-message');
    if (messageDiv) {
      messageDiv.textContent = message;
      messageDiv.classList.remove('success', 'error');
      messageDiv.classList.add(type);
      messageDiv.style.display = 'block';

      if (type === 'success') {
        setTimeout(() => {
          messageDiv.style.display = 'none';
        }, 7000);
      }
    }
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

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeInvolveModal();
  });

  console.log('Engolon CBO website loaded successfully!');
});
