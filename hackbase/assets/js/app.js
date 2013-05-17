var app = angular.module('app', ['mongolab']).
  config(function($routeProvider) {
    $routeProvider.
      when('/', {controller: ListCtrl, templateUrl: 'static/templates/list.html'}).
      when('/edit/:projectId', {controller: EditCtrl, templateUrl: 'static/templates/detail.html'}).
      when('/new', {controller: CreateCtrl, templateUrl: 'static/templates/detail.html'}).
      otherwise({redirectTo: '/'});
  });

// An example filter that reverses a string
// Filters that come with angular:
// orderBy
// search:'name'    for example, where name is a prop on the repeat
app.filter('reverse', function() {
  return function (text) {
    return text.split('').reverse().join('');
  }
});

// This is a directive, use it to apply behavior to a class, attribute or element
app.directive('enter', function() {
  return function ($scope, element) {
    element.bind('mouseenter', function() {
      $scope.$apply(attrs.enter); // supply enter="loadMoreTweets"
      // and specify loadMoreTweets on the controller's scope
    });
  }
});

function ListCtrl($scope, Project) {
  $scope.projects = Project.query();
}

function CreateCtrl($scope, $location, Project) {
  $scope.save = function () {
    Project.save($scope.project, function(project) {
      $location.path('/edit/' + project._id.$oid);
    });
  }
}

function EditCtrl($scope, $location, $routeParams, Project) {
  var self = this;

  Project.get({id: $routeParams.projectId}, function(project) {
    self.original = project;
    $scope.project = new Project(self.original);
  });

  $scope.isClean = function () {
    return angular.equals(self.original, $scope. project);
  };

  $scope.destroy = function () {
    self.original.destroy(function () {
      $location.path('/list');
    });
  };

  $scope.save = function () {
    $scope.project.update(function() {
      $location.path('/');
    });
  };
}

