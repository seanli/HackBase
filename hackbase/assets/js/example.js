function IndexCtrl($scope) {

  $scope.current_user = null;

  /*$scope.fb_ref = new Firebase('https://hackbase.firebaseio.com/');
  $scope.auth_client = new FirebaseAuthClient($scope.fb_ref, function(error, user) {
    if (error) {
      // an error occurred while attempting login
      console.log(error);
    } else if (user) {
      // user authenticated with Firebase
      var users = new Firebase('https://hackbase.firebaseio.com/users');
      users.child(user.id).once('value', function(snapshot) {
        if (snapshot.val() === null) {
          var userRef = new Firebase('https://hackbase.firebaseio.com/users/' + user.id);
          userRef.set({first_name: user.first_name, last_name: user.last_name, email: user.email});
          console.log(user);
        } else {
          $scope.current_user = {};
          $scope.current_user['username'] = user.username;
        }
      });
    } else {
      $scope.current_user = null;
    }
  });*/

  $scope.login = function() {
    $scope.current_user = 'LOGGEDIN!';
  };

  $scope.logout = function() {
    $scope.current_user = null;
  };

}