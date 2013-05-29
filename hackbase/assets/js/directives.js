var directives = {};
app.directive(directives);

directives.todo = function() {
  return {
    restrict: 'E',
    transclude: true,
    scope: {},
    templateUrl: '/static/templates/todo.html',
    controller: function($scope, $element, $attrs, angularFire, angularFireCollection) {
      var url = 'https://test123412.firebaseio.com/' + 1 + '/todo';
      $scope.todos = angularFireCollection(url);

      $scope.addTodo = function () {
        if (!$scope.newTodo.length) {
          return;
        }

        $scope.todos.add({
          text: $scope.newTodo,
          done: false
        }, function() {});

        $scope.newTodo = '';
      };

      $scope.editTodo = function (todo) {
        $scope.editedTodo = todo;
      };

      $scope.doneEditing = function (todo) {
        $scope.editedTodo = null;
        if (!todo.title) {
          $scope.removeTodo(todo);
        }
      };

      $scope.removeTodo = function (todo) {
        $scope.todos.splice($scope.todos.indexOf(todo), 1);
      };
    },
  }
};
