// Reading progress enhances the table of contents; all navigation is ordinary links.
const headings = [...document.querySelectorAll('.body h2, .body h3')];
if (headings.length) {
  let pending = false;
  const update = () => {
    const current = headings.filter(node => node.getBoundingClientRect().top <= 120).at(-1) || headings[0];
    document.querySelectorAll('.toc a').forEach(link => {
      if (link.hash === `#${current.id}`) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
    pending = false;
  };
  addEventListener('scroll', () => {
    if (!pending) { pending = true; requestAnimationFrame(update); }
  }, { passive: true });
  update();
}

const screenLinks = [...document.querySelectorAll('[data-screen]')];
if (screenLinks.length && typeof HTMLDialogElement !== 'undefined') {
  const dialog = document.createElement('dialog');
  dialog.className = 'screen-dialog';
  dialog.setAttribute('aria-label', 'Full-size interface');
  const close = document.createElement('button');
  close.type = 'button';
  close.textContent = 'Close ×';
  const fullImage = document.createElement('img');
  dialog.append(close, fullImage);
  document.body.append(dialog);
  screenLinks.forEach(link => link.addEventListener('click', event => {
    if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    fullImage.src = link.href;
    fullImage.alt = link.querySelector('img').alt;
    dialog.showModal();
    dialog.scrollTop = 0;
  }));
  close.addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => {
    if (event.target === dialog) {
      const bounds = dialog.getBoundingClientRect();
      if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
    }
  });
}
