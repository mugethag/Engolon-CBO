# Course Access Control

The `robotics-certificate.html` page currently uses a lightweight browser-side password gate.

Temporary access password:

```text
EngolonCourse2026!
```

## How It Works

- The protected course content is hidden by default with CSS.
- `assets/js/course-auth.js` checks the entered password against a SHA-256 hash.
- Successful access is remembered in `localStorage` for that browser.

## Important Security Note

This is suitable for controlled previews and casual access control only. Because the Engolon site is currently static, determined users could still inspect source files or directly request linked assets if they know the paths.

For real student access control, use one of these:

- An LMS such as Moodle, Canvas, Google Classroom, or Thinkific.
- Netlify/serverless authentication that serves protected course files only after login.
- A member portal backed by a database and server-side sessions.

## Changing The Password

1. Generate a new SHA-256 hash for the desired password.
2. Replace `COURSE_PASSWORD_HASH` in `assets/js/course-auth.js`.
3. Share the new password with approved students.
