var myApp=angular.module('myApp', []);
myApp.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{$').endSymbol('$}');
});

myApp.controller('PhoneListCtrl', function($scope, $http){
    $http.get('http://localhost:8000/api/payments.json').success(function(data){
       $scope.payments = data;
    });

    $scope.sortField = undefined;
    $scope.reverse = false

    $scope.sort = function(fieldName){
        if($scope.sortField === fieldName){
            $scope.reverse = !$scope.reverse;
        }
        else {
            $scope.sortField = fieldName;
            $scope.reverse = false;
        }

    };

    $scope.isSortUp = function(fieldName){
        return $scope.sortField === fieldName && !$scope.reverse;
    }

    $scope.isSortDown = function(fieldName){
        return $scope.sortField === fieldName && $scope.reverse;
    }
});