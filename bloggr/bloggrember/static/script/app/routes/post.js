App.PostRoute = Ember.Route.extend({
  model: function(params) {
    return this.store.find('post', params.photo_id);
  }
});