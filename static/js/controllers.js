'use strict';

/* Controllers */

angular.module('BannedApp.controllers', []).
  controller('ReplaceCtrl', ['$scope', '$http', function($scope, $http) {
      $scope.output = '';

      $scope.submit_ajax_input = function() {
          $http({
              url:'/replace',
              data: JSON.stringify({'input': $scope.input}),
              headers: {
                "Content-Type": "application/json; charset=utf-8"
              },
              method:'POST'})
              .success(function(data) {
                  $scope.output = data;
              });
      };

      $scope.submit_ajax_input2 = function() {
          $http({
              url:'/ac_replace',
              data: JSON.stringify({'input': $scope.input2}),
              headers: {
                "Content-Type": "application/json; charset=utf-8"
              },
              method:'POST'})
              .success(function(data) {
                  $scope.output2 = data;
              });
      };

  }])
  .controller('MyCtrl2', [function() {

  }]);
