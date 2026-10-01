/* ============================================================
   Taylor's Earth Works - JavaScript Utilities
   - Before/After Interactive Slider
   - Mobile Nav Toggle
   - Free Contact Form Handler (AJAX + FormSubmit/Web3Forms)
   - Smooth Scroll & Year Auto-update
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Current Year in Footer
  const yearElement = document.getElementById('current-year');
  if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
  }

  // 2. Mobile Menu Toggle
  const mobileToggle = document.getElementById('mobile-toggle');
  const mobileMenu = document.getElementById('mobile-menu');

  if (mobileToggle && mobileMenu) {
    mobileToggle.addEventListener('click', () => {
      mobileMenu.classList.toggle('active');
    });

    // Close menu when clicking any nav link
    const mobileLinks = mobileMenu.querySelectorAll('a');
    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.remove('active');
      });
    });
  }

  // 3. Before & After Comparison Slider
  initBeforeAfterSlider();

  // 4. Contact / Estimate Form AJAX Submission
  initEstimateForm();
});

/**
 * Interactive Before / After Slider with Drag and Touch Support
 */
function initBeforeAfterSlider() {
  const container = document.querySelector('.ba-container');
  const beforeDiv = document.querySelector('.ba-before');
  const handle = document.querySelector('.ba-handle');

  if (!container || !beforeDiv || !handle) return;

  let isDragging = false;

  function updateSliderPosition(clientX) {
    const rect = container.getBoundingClientRect();
    let offsetX = clientX - rect.left;
    let percentage = (offsetX / rect.width) * 100;

    // Constrain between 0% and 100%
    if (percentage < 0) percentage = 0;
    if (percentage > 100) percentage = 100;

    beforeDiv.style.width = `${percentage}%`;
    handle.style.left = `${percentage}%`;
  }

  // Ensure the clipped image matches the exact width & height of the container
  const beforeImg = beforeDiv.querySelector('.ba-image');
  function syncImageDimensions() {
    if (beforeImg && container) {
      beforeImg.style.width = `${container.offsetWidth}px`;
      beforeImg.style.height = `${container.offsetHeight}px`;
    }
  }
  syncImageDimensions();
  window.addEventListener('resize', syncImageDimensions);
  window.addEventListener('load', syncImageDimensions);
  if (beforeImg) {
    beforeImg.addEventListener('load', syncImageDimensions);
  }


  // Mouse Events
  handle.addEventListener('mousedown', () => {
    isDragging = true;
  });

  window.addEventListener('mouseup', () => {
    isDragging = false;
  });

  window.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    updateSliderPosition(e.clientX);
  });

  // Touch Events for Mobile / Tablet
  handle.addEventListener('touchstart', () => {
    isDragging = true;
  }, { passive: true });

  window.addEventListener('touchend', () => {
    isDragging = false;
  });

  window.addEventListener('touchmove', (e) => {
    if (!isDragging || !e.touches[0]) return;
    updateSliderPosition(e.touches[0].clientX);
  }, { passive: true });

  // Direct Click on Container to Jump
  container.addEventListener('click', (e) => {
    updateSliderPosition(e.clientX);
  });
}

/**
 * Estimate Form Handling
 * Configured to work seamlessly with FormSubmit.co (100% free)
 * Sends as JSON/AJAX for a seamless, app-like user experience.
 */
function initEstimateForm() {
  const form = document.getElementById('estimate-form');
  const submitBtn = document.getElementById('submit-btn');
  const alertSuccess = document.getElementById('form-success');
  const alertError = document.getElementById('form-error');

  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Check honeypot for spam bots
    const honeypot = form.querySelector('input[name="_honey"]');
    if (honeypot && honeypot.value) {
      console.warn('Bot submission blocked.');
      return;
    }

    const originalBtnText = submitBtn ? submitBtn.innerHTML : 'Send Request';
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.innerHTML = 'Sending Request...';
    }

    if (alertSuccess) alertSuccess.style.display = 'none';
    if (alertError) alertError.style.display = 'none';

    const formData = new FormData(form);

    try {
      const response = await fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
          'Accept': 'application/json'
        }
      });

      if (response.ok) {
        if (alertSuccess) {
          alertSuccess.style.display = 'block';
          alertSuccess.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
        form.reset();
      } else {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.message || 'Submission failed');
      }
    } catch (err) {
      console.error('Form submission error:', err);
      if (alertError) {
        alertError.style.display = 'block';
        alertError.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    } finally {
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.innerHTML = originalBtnText;
      }
    }
  });
}
