var directives = {};
app.directive(directives);

directives.todo = function() {
  return {
    restrict: 'E',
    transclude: false,
    scope: {},
    templateUrl: '/static/templates/todo.html',
    controller: function($scope, $element, angularFire) {
      var url = 'https://test123412.firebaseio.com/' + 1 + '/todo';
      var promise = angularFire(url, $scope, 'todos');

      var startWatch = function ($scope) {
        // registers a callback whenever the scope member 'todos' changes
        $scope.addTodo = function () {
          if (!$scope.newTodo.length) {
            return;
          }

          $scope.todos.push({
            text: $scope.newTodo,
            done: false
          });

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
      }

      promise.then(function(todos) {
        startWatch($scope);
      });
    },
  }
};
