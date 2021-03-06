import Ember from 'ember';

export default Ember.Route.extend({
  actions: {
    error: function(error){
      console.log(error);
      if (error.status === 0) {
        this.send("setTitle", gettext('Connection lost'));
        return this.intermediateTransitionTo('error0');
      }

      if (error.status === 403) {
        this.send("setTitle", gettext('Page not available'));

        var final_error = {status: 403, message: null};
        if (error.responseJSON.detail !== "Permission denied") {
          final_error.message = error.responseJSON.detail;
        }

        return this.intermediateTransitionTo('error403', final_error);
      }

      if (error.status === 404) {
        this.send("setTitle", gettext('Page not found'));
        return this.intermediateTransitionTo('error404');
      }
    },

    setTitle: function(title) {
      if (typeof title === "string") {
        title = {title: title};
      }

      var complete_title = title.title;
      complete_title += " | " + this.get('settings.forum_name');

      document.title = complete_title;
      return false;
    }
  }
});
