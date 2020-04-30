
import pandas as pd
from spyre import server


class WebApp(server.App):
    title = "Lab 2"
    inputs = [
        {
            "type": "dropdown",
            "id": "region",
            "label": "Область",
            "key": 'region',

            "options": [
                {"label": "Cherkasy ", "value": 'info_region_1.csv'},
                {"label": "Chernihiv ", "value": 'info_region_2.csv'},
                {"label": "Chernivtsi ", "value": 'info_region_3.csv'},
                {"label": "Crimea ", "value": 'info_region_4.csv'},
                {"label": "Dnipropetrovsk ", "value": 'info_region_5.csv'},
                {"label": "Donetsk ", "value": 'info_region_6.csv'},
                {"label": "Ivano-Frankivsk ", "value": 'info_region_7.csv'},
                {"label": "Kharkiv ", "value": 'info_region_8.csv'},
                {"label": "Kherson ", "value": 'info_region_9.csv'},
                {"label": "Khmelnytskyy ", "value": 'info_region_10.csv'},
                {"label": "Kiev", "value": 'info_region_11.csv'},
                {"label": "Kirovohrad ", "value": 'info_region_13.csv'},
                {"label": "Luhansk ", "value": 'info_region_14.csv'},
                {"label": "Lviv ", "value": 'info_region_15.csv'},
                {"label": "Mykolayiv ", "value": 'info_region_16.csv'},
                {"label": "Odessa ", "value": 'info_region_17.csv'},
                {"label": "Poltava ", "value": 'info_region_18.csv'},
                {"label": "Rivne ", "value": 'info_region_19.csv'},
                {"label": "Sumy ", "value": 'info_region_21.csv'},
                {"label": "Ternopil ", "value": 'info_region_22.csv'},
                {"label": "Transcarpathia ", "value": 'info_region_23.csv'},
                {"label": "Vinnytsya ", "value": 'info_region_24.csv'},
                {"label": "Volyn ", "value": 'info_region_25.csv'},
                {"label": "Zaporizhzhya ", "value": 'info_region_26.csv'},
                {"label": "Zhytomyr ", "value": 'info_region_27.csv'}
            ],

            "value": "info_region_11.csv",
            "action_id": "update_data"
        },

        {
            "type": "dropdown",
            "id": "year",
            "label": "Год",

            "options": [
                {"label": year, "value": year} for year in range(1982, 2021)
            ],

            "key": "year",
            "action_id": "update_data"
        },

        {
            "type": "dropdown",
            "id": "week",
            "label": "Неделя c",
            "options": [
                {"label": week_from, "value": week_from} for week_from in range(1, 53)
            ],
            "key": "week_from",
            "action_id": "update_data"
        },

        {
            "type": "dropdown",
            "id": "week",
            "label": "Неделя по",
            "options": [
                {"label": week_to, "value": week_to} for week_to in range(1, 53)
            ],
            "key": "week_to",
            "action_id": "update_data"
        },

        {
            "type": "dropdown",
            # "id": "index",
            "label": "Индексы",
            "options": [

                {"label": "VHI", "value": "VHI"},

                {"label": "TCI", "value": "TCI"},

                {"label": "VCI", "value": "VCI"}

            ],
            "key": "index",
            "action_id": "update_data"
        }

    ]

    controls = [{"type": "hidden",
                 "id": "update_data"}]


    tabs = ["Table", "Plot"]
    outputs = [

        {
            "type": "table",
            "id": "Data",
            "control_id": "update_data",
            "tab": "Table",
            "on_page_load": True
        },

        {
            "type": "plot",
            "id": "Plot",
            "control_id": "update_data",
            "tab": "Plot"
        }
    ]

    def Data(self, params):
        region = params["region"]
        year = int(params["year"])
        week_from = int(params["week_from"])
        week_to = int(params["week_to"])

        df = pd.read_csv("csv/" + region)
        # df = df.loc[df.year == year]
        # filtered_data = df[(df.week >= week_from) & (df.week <= week_to)]
        filtered_data = df[(df.week >= week_from) & (df.week <= week_to) & (df.year == year)]
        return filtered_data




    def Plot(self, params):

        oy = params["index"]
        year = params["year"]
        week_from = params["week_from"]
        week_to = params["week_to"]

        df = self.Data(params)
        plot_obj = df.plot(x='week', y=oy)


        plot_obj.set_title(oy + " for the selected period of " + year)
        plot_obj.set_ylabel(oy + ", %")
        plot_obj.set_xlabel("Selected period: weeks from " + week_from + " to " + week_to + " of " + year)
        fig = plot_obj.get_figure()
        return fig


app = WebApp()
app.launch(port=9098)
