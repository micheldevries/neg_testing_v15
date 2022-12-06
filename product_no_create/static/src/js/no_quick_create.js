odoo.define("product_no_create.no_quick_create", function (require) {
    "use strict";

    var relational_fields = require("web.relational_fields");
    var Dialog = require("web.Dialog");
    var core = require("web.core");
    var _t = core._t;

    var M2ODialog = Dialog.extend({
        template: "M2ODialog",
        init: function (parent, name, value) {
            this.name = name;
            this.value = value;
            this._super(parent, {
                title: _.str.sprintf(_t("New %s"), this.name),
                size: "medium",
                buttons: [
                    {
                        text: _t("Create"),
                        classes: "btn-primary",
                        close: true,
                        click: function () {
                            this.trigger_up("quick_create", {value: this.value});
                        },
                    },
                    {
                        text: _t("Discard"),
                        close: true,
                    },
                ],
            });
        },
        /**
         * @override
         * @param {Boolean} isSet
         */
        close: function (isSet) {
            this.isSet = isSet;
            this._super.apply(this, arguments);
        },
        /**
         * @override
         */
        destroy: function () {
            if (!this.isSet) {
                this.trigger_up("closed_unset");
            }
            this._super.apply(this, arguments);
        },
    });

    relational_fields.FieldMany2One.include({
        _onInputFocusout: function () {
            if (!this.floating) {
                return;
            }
            const firstValue = this.suggestions.find((s) => s.id);
            if (firstValue) {
                this.reinitialize({id: firstValue.id, display_name: firstValue.name});
            } else if (this.can_create) {
                if (this.nodeOptions && !this.nodeOptions.no_quick_create) {
                    new M2ODialog(this, this.string, this.$input.val()).open();
                }
            } else {
                this.$input.val("");
            }
        },
    });
});
