app.animation('fade-enter', function () {
  return {
    setup: function (element) {
      $(element).hide();
    },
    start: function (element, done, memo) {
      $(element).fadeIn(400, function() {
        done();
      });
    }
  };
});
