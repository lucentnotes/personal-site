# Lucy Yu homepage

The root `index.html` is the approved English-default bilingual homepage. `home-assets/` contains versioned local fonts, the user-approved logo, original project stills and muted real project recordings.

The homepage uses three full-screen sections: introduction, work carousel, contact. `?lang=zh` selects Chinese; an unqualified root URL always starts in English. Links explicitly carry the selected language. The existing case and story scripts now also default to English and respect an explicit Chinese parameter. Existing articles and project layouts are preserved.

Contact is configured through FormSubmit. Mailbox activation and actual message delivery still need confirmation by the site owner; browser checks do not send a message.

Deploy only changes on top of the current gh-pages tree. Do not run the historical single-section build and replace this tree: that would delete newer project and story pages.

The recordings show an actual game operation sequence from the gameplay repository and a silent excerpt of the published Act I film. The game is not represented by the earlier weights-editor prototype. Font license notices are in home-assets.
