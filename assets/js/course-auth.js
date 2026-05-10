// Lightweight course gate for preview access.
// For production student records, use an LMS or server-side authentication.

const COURSE_PASSWORD_HASH = 'abcfca821ac0b195c964569cd819b8c6d6634b086771bab862dacb24680fa945';
const COURSE_AUTH_KEY = 'engolon-course-access';

async function hashCoursePassword(value) {
  const data = new TextEncoder().encode(value);
  const digest = await crypto.subtle.digest('SHA-256', data);
  return Array.from(new Uint8Array(digest))
    .map(byte => byte.toString(16).padStart(2, '0'))
    .join('');
}

function unlockCourse() {
  document.body.classList.remove('course-locked');
  document.body.classList.add('course-unlocked');

  const loginSection = document.getElementById('course-login');
  const protectedContent = document.getElementById('course-protected-content');

  if (loginSection) {
    loginSection.setAttribute('aria-hidden', 'true');
  }

  if (protectedContent) {
    protectedContent.setAttribute('aria-hidden', 'false');
  }
}

document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('course-login-form');
  const input = document.getElementById('course-password');
  const message = document.getElementById('course-login-message');

  if (localStorage.getItem(COURSE_AUTH_KEY) === COURSE_PASSWORD_HASH) {
    unlockCourse();
    return;
  }

  if (!form || !input || !message) return;

  form.addEventListener('submit', async function (event) {
    event.preventDefault();

    const candidateHash = await hashCoursePassword(input.value);

    if (candidateHash === COURSE_PASSWORD_HASH) {
      localStorage.setItem(COURSE_AUTH_KEY, candidateHash);
      message.textContent = 'Access granted.';
      message.className = 'form-message success course-login-message';
      unlockCourse();
      return;
    }

    message.textContent = 'Incorrect password. Please check your course access details.';
    message.className = 'form-message error course-login-message';
    input.value = '';
    input.focus();
  });
});
