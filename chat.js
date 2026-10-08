// Let's Chat launcher, ported from the client sites (blessyourpaws, mldesigns, cornerstonesvcs,
// teapup, sweetpuppypaws). It is a contact launcher, not live chat: a button that opens a small
// panel with call or text, email, and the project form.
(function(){
  // A page that already carries the form does not need a launcher for it, and on a phone
  // the fixed button lands on top of a form field.
  if (document.querySelector('main form')) return;

  var fab = document.createElement('button');
  fab.type = 'button';
  fab.className = 'chat-fab';
  fab.setAttribute('aria-expanded', 'false');
  fab.setAttribute('aria-controls', 'chatPanel');
  fab.setAttribute('aria-label', 'Chat with Alex');
  fab.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg><span class="fab-label">Let’s Chat</span>';

  var panel = document.createElement('div');
  panel.className = 'chat-panel';
  panel.id = 'chatPanel';
  panel.setAttribute('role', 'dialog');
  panel.setAttribute('aria-label', 'Contact options');
  panel.innerHTML = '<h3>Talk through your website</h3>'
    + '<p>Call or text is the quickest way to reach me.</p>'
    + '<div class="row"><span class="lbl">Call or text</span><a href="tel:+15025093105">(502) 509-3105</a></div>'
    + '<div class="row"><span class="lbl">Email</span><a href="mailto:alex@harperstudio.co">alex@harperstudio.co</a></div>'
    + '<div class="row"><span class="lbl">Project</span><a href="contact.html">Tell me about your website</a></div>';

  document.body.appendChild(panel);
  document.body.appendChild(fab);

  function set(open){
    panel.classList.toggle('open', open);
    fab.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  fab.addEventListener('click', function(){ set(!panel.classList.contains('open')); });
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape' && panel.classList.contains('open')) { set(false); fab.focus(); }
  });
})();
