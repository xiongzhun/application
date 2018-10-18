# -*- coding: utf-8 -*-

from __future__ import absolute_import
import xadmin
from xadmin import views
from .models import IDC, Cabinet, Switch, Host, HostGroup, Port
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction


@xadmin.sites.register(views.website.IndexView)
class MainDashboard(object):
    widgets = [
        [
            {"type": "qbutton", "title": "Quick Start",
             "btns": [{"model": Host}, {"model": IDC}, {"model": Cabinet}]},
            {"type": "addform", "model": Cabinet},
        ]
    ]


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    global_search_models = [Host, IDC]
    global_models_icon = {
        Host: "fa fa-laptop", IDC: "fa fa-cloud",Switch: "fa fa-random", HostGroup: "fa fa-group", Port: "fa fa-book", Cabinet:"fa fa-tasks"
    }
    menu_style = 'default'  # 'accordion'


class PortInline(object):
    model = Port
    extra = 1
    style = "accordion"


@xadmin.sites.register(IDC)
class IDCAdmin(object):
    list_display = ("name", "description", "contact", "telphone", "address")
    list_display_links = ("name",)
    wizard_form_list = [
        ("First's Form", ("name", "description")),
        ("Second Form", ("contact", "telphone", "address")),
    ]
    search_fields = ["name", "description", "contact", "telphone", "address"]
    list_filter = [
        "name"
    ]
    list_quick_filter = [{"field": "name", "limit": 10}]

    search_fields = ["name"]
    relfield_style = "fk-select"
    reversion_enable = True

    actions = [BatchChangeAction, ]
    batch_fields = ("contact", "description", "address")

@xadmin.sites.register(Cabinet)
class CabinetAdmin(object):
    list_display = ("name", "idc")
    list_display_links = ("name",)

    search_fields = ["name"]
    style_fields = {"hosts": "checkbox-inline"}


@xadmin.sites.register(Switch)
class SwitchAdmin(object):
    list_display = ("name", "sn", "cabinet", "up_port", "ip", "user", "password")

    search_fields = ["ip"]
    style_fields = {"hosts": "checkbox-inline"}

@xadmin.sites.register(Host)
class HostAdmin(object):
    def open_web(self, instance):
        return """<a href="http://%s" target="_blank">Open</a>""" % instance.ip

    open_web.short_description = "Acts"
    open_web.allow_tags = True
    open_web.is_column = True

    list_display = (
        "name", "idc", "host_group", "status",
        "info", "left", "description", "ip",
    )
    list_display_links = ("name",)

    raw_id_fields = ("idc",)
    style_fields = {"system": "radio-inline"}

    search_fields = ["name", "ip", "description"]
    list_filter = [
        "idc", "host_group", "cabinet", "guarantee_date", "status", "brand", "hard_disk", "memory", "left"
    ]

    list_quick_filter = [{"field": "idc__name", "limit": 10}]
    # list_quick_filter = ["idc_id"]
    list_bookmarks = [{
        "title": "Need Guarantee",
        "query": {"status_exact": 2},
        "order": ("guarantee_date",),
        "cols": ("brand", "guarantee_date"),
    }]

    show_detail_fields = ("idc",)
    list_editable = (
        "name", "idc", "info", "description", "ip", "left"
    )
    save_as = True

    aggregate_fields = {"guarantee_date": "min"}
    grid_layouts = ("table", "thumbnails")

    form_layout = (
        Main(
            TabHolder(
                Tab(
                    "Comm Fields",
                    Fieldset(
                        "Company data", "name", "idc", "cabinet", "address_number", "ip", "internal_ip", "user", "password", "host_group", "administrator", "left", "guarantee_date", "system_user", "system_password",
                        description = "some comm fields, required",
                    ),
                    Inline(Port)
                ),
                Tab(
                    "Extend Fields",
                    Fieldset(
                        "Contact details",
                        Row("brand", "model"),
                        Row("cpu"),
                        Row(
                            AppendedText("hard_disk", "G"),
                            AppendedText("memory", "G")
                        ),
                    ),
                ),
            ),
        ),
        Side(
            Fieldset("Status data", "status"),
        )
    )
    inlines = [PortInline]
    reversion_enable = True

    data_charts = {
        "host_service_type_counts": {'title': u"Host service type count", "x-field": "host_group",
                                     "y-field": ("host_group",),
                                     "option": {
                                         "series": {"bars": {"align": "center", "barWidth": 0.8, 'show': True}},
                                         "xaxis": {"aggregate": "count", "mode": "categories"},
                                     },
                                     },
    }


@xadmin.sites.register(HostGroup)
class HostGroupAdmin(object):
    list_display = ("name", "description")
    list_display_links = ("name",)

    search_fields = ["name"]
    style_fields = {"hosts": "checkbox-inline"}


@xadmin.sites.register(Port)
class PortAdmin(object):
    list_display = ("host", "name", "switch_port")


# xadmin.sites.site.register(HostGroup, HostGroupAdmin)
# xadmin.sites.site.register(IDC, IDCAdmin)
# xadmin.sites.site.register(AccessRecord, AccessRecordAdmin)
