// Onsite, wrap this in a script tag if placed in body or header
// This works off the parent div aria label down to the closest anchors, pulls attribute data and passes to a track event call 
// Allows us to keep naming convention clean, keep low cardinality in event naming, and use event props 

document.addEventListener('DOMContentLoaded', function() {
  var socialParent = document.querySelector('div[aria-label="social_parent"]');

  socialParent.addEventListener('click', function(event) {
    var targetElement = event.target.closest('a');

    if (targetElement) {
      var linkName = targetElement.getAttribute('name');
      var linkHref = targetElement.getAttribute('href');

      // Segment track call for any link clicked below the social_parent container
      analytics.track('Clicked Social Link', {
        name: linkName,
        href: linkHref
      });
    }
  });
});