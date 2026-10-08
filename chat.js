// "Let's chat" launcher, in the same format as Teapup and Sweet Puppy Paws: a close button,
// a heading and one line, then labeled rows that always present a way to reach Alex. It is a
// contact launcher, not live chat.
//
// It does not appear on a page whose main holds a form, because on a phone a fixed button
// in the bottom-right corner lands on a form field. It hides while the menu is open, through
// body.nav-open in studio.css.
(function(){
  'use strict';
  if (document.querySelector('main form')) return;

  // The value is one element, always. The row is a two-column grid, and the call line puts
  // two links in it, so loose they would drop "text" onto a second row under the label.
  function row(label, inner){
    return '<div class="row"><span class="lbl">' + label + '</span>'
      + '<span class="v">' + inner + '</span></div>';
  }

  var fab = document.createElement('button');
  fab.type = 'button';
  fab.className = 'chat-fab';
  fab.setAttribute('aria-expanded', 'false');
  fab.setAttribute('aria-controls', 'chatPanel');
  fab.setAttribute('aria-label', 'Talk to Alex about your website');
  fab.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg><span class="fab-label">Let’s chat</span>';

  var panel = document.createElement('div');
  panel.className = 'chat-panel';
  panel.id = 'chatPanel';
  panel.setAttribute('role', 'dialog');
  panel.setAttribute('aria-label', 'Talk to Alex about your website');
  panel.innerHTML = '<button type="button" class="shut" aria-label="Close">&times;</button>'
    + '<h2>Talk to me about your website</h2>'
    + '<p>Call or text is the quickest way to reach me.</p>'
    + row('Call or text', '<a href="tel:+15025093105">(502) 509-3105</a>'
        + ' <a class="alt" href="sms:+15025093105">text</a>')
    + row('Email', '<a href="mailto:alex@harperstudio.co">alex@harperstudio.co</a>')
    + row('Start', '<a href="contact.html">Tell me about your website</a>')
    + row('Pricing', '<a href="plans.html">See build and care prices</a>')
    + row('Where', '<span class="val">New Albany, Indiana</span>');

  document.body.appendChild(panel);
  document.body.appendChild(fab);

  function set(open){
    panel.classList.toggle('open', open);
    fab.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  fab.addEventListener('click', function(){ set(!panel.classList.contains('open')); });
  panel.querySelector('.shut').addEventListener('click', function(){ set(false); fab.focus(); });
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape' && panel.classList.contains('open')) { set(false); fab.focus(); }
  });
  // tapping the page behind it closes it
  document.addEventListener('click', function(e){
    if (!panel.classList.contains('open')) return;
    if (panel.contains(e.target) || fab.contains(e.target)) return;
    set(false);
  });
})();
