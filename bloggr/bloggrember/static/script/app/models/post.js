App.Post = DS.Model.extend({
  title: DS.attr('string'),
  date: DS.attr('string'),
  author: DS.attr('string'),
  excerpt: DS.attr('string'),
  body: DS.attr('string'),
});