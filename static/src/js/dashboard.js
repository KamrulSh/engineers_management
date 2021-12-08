odoo.define('engineers_management.DashboardRewrite', function (require) {
    "use strict";

    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var EngineerDashboard = AbstractAction.extend({
        template: 'EngineerDashboardMain',

    });

    core.action_registry.add('engineer_dashboard_tag', EngineerDashboard);

    return EngineerDashboard;

});