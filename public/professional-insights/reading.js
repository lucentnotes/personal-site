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
