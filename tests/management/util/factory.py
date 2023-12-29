import pandas as pd

from data_models.models import Land, PrefecturesCity, RegistrationMap


class ChisekiDataFrameFactory(object):
    @property
    def tokyo_data(self):
        """
        東京：公共座標9系と任意座標系の混在
        """
        c1 = [
            [
                [
                    [139.764068706, 35.687606251],
                    [139.764852998, 35.687524233],
                    [139.766223114, 35.687380921],
                    [139.766187703, 35.687236276],
                    [139.764025551, 35.687465459],
                    [139.764068706, 35.687606251],
                ]
            ]
        ]
        c2 = [
            [
                [
                    [139.76109229, 35.690769979],
                    [139.761218, 35.69066656],
                    [139.761739878, 35.690261254],
                    [139.761794413, 35.69022735],
                    [139.761851486, 35.690197387],
                    [139.761914599, 35.690171095],
                    [139.76200413, 35.690144495],
                    [139.762335077, 35.690086624],
                    [139.762350559, 35.69008392],
                    [139.762251096, 35.689287167],
                    [139.76182575, 35.689321375],
                    [139.761759154, 35.689326743],
                    [139.761122383, 35.689378075],
                    [139.761112054, 35.689412888],
                    [139.76110126, 35.689449207],
                    [139.761072867, 35.689567891],
                    [139.761057578, 35.68968817],
                    [139.761055535, 35.689809079],
                    [139.761056236, 35.689828125],
                    [139.76109229, 35.690769979],
                ]
            ]
        ]
        c3 = [
            [
                [
                    [1264.595, 539.55],
                    [1265.6, 521.941],
                    [1267.792, 520.309],
                    [1272.858, 516.538],
                    [1275.033, 517.351],
                    [1293.805, 524.365],
                    [1319.481, 537.418],
                    [1333.5, 544.424],
                    [1328.619, 584.018],
                    [1327.406, 593.46],
                    [1326.43, 601.068],
                    [1316.504, 682.587],
                    [1309.829, 682.239],
                    [1319.517, 693.035],
                    [1336.227, 689.753],
                    [1399.636, 671.8],
                    [1483.502, 649.21],
                    [1465.212, 573.011],
                    [1383.53, 561.817],
                    [1345.252, 541.168],
                    [1333.754, 534.459],
                    [1298.572, 516.523],
                    [1293.987, 514.813],
                    [1262.203, 503.068],
                    [1261.943, 500.212],
                    [1259.97, 501.756],
                    [1264.595, 539.55],
                ]
            ]
        ]
        pd.options.display.float_format = "{:.2f}".format
        return pd.DataFrame(
            {
                "address": ["千代田区大手町１丁目15-21", "千代田区大手町１丁目7-28", "台東区浅草２丁目66-1"],
                "市区町村コード": ["13101", "13101", "13101"],
                "座標系": ["公共座標9系", "公共座標9系", "任意座標系"],
                "coordinates": [c1, c2, c3],
                "面積正解": [3182.7, 12560.6, 17361],
            }
        )

    @property
    def okinawa_only_public(self):
        """
        沖縄：公共座標系のみ
        """
        c4 = [
            [
                [
                    [127.740106995, 26.274760635],
                    [127.739912279, 26.274609446],
                    [127.739659033, 26.274873712],
                    [127.739985264, 26.275131928],
                    [127.740031362, 26.274951587],
                    [127.740106995, 26.274760635],
                ]
            ]
        ]
        c5 = [
            [
                [
                    [127.759048194, 26.319470816],
                    [127.758912153, 26.319800635],
                    [127.759102997, 26.319859208],
                    [127.759174051, 26.319691517],
                    [127.759248632, 26.31950211],
                    [127.759048194, 26.319470816],
                ]
            ]
        ]
        c6 = [
            [
                [
                    [127.763181847, 26.353252576],
                    [127.763462641, 26.353280151],
                    [127.763667421, 26.353216091],
                    [127.763586812, 26.353041845],
                    [127.763557743, 26.352979019],
                    [127.76336138, 26.352715865],
                    [127.763074793, 26.352717863],
                    [127.763139812, 26.353042667],
                    [127.763181847, 26.353252576],
                ]
            ]
        ]
        pd.options.display.float_format = "{:.2f}".format
        return pd.DataFrame(
            {
                "address": ["宜野湾市大山６丁目8-4", "中頭郡北谷町２丁目8-1", "中頭郡嘉手納町字野里大城原529"],
                "座標系": ["公共座標15系", "公共座標15系", "公共座標15系"],
                "市区町村コード": ["47205", "47326", "47325"],
                "coordinates": [c4, c5, c6],
                "面積正解": [1308.86, 819.9, 2476],
            }
        )

    @property
    def hokkaido_multi_public(self):
        """
        北海道：公共座標系混在
        混在していてもエラーにならない
        """
        c4 = [
            [
                [
                    [140.822882826, 41.793496962],
                    [140.822896605, 41.793494436],
                    [140.822897663, 41.793467355],
                    [140.823127042, 41.793452155],
                    [140.82352186, 41.793440667],
                    [140.823617994, 41.793363345],
                    [140.823921048, 41.793349792],
                    [140.824018525, 41.793413623],
                    [140.824073012, 41.793449295],
                    [140.824109434, 41.793481673],
                    [140.824228402, 41.793587436],
                    [140.824386738, 41.793724013],
                    [140.824495817, 41.793845979],
                    [140.824520671, 41.793873759],
                    [140.824678014, 41.794010854],
                    [140.824768336, 41.794108621],
                    [140.824926311, 41.794234178],
                    [140.825032628, 41.79434447],
                    [140.825200825, 41.794518976],
                    [140.825274703, 41.794595637],
                    [140.825452727, 41.794780332],
                    [140.8254968, 41.794757268],
                    [140.825460712, 41.794727374],
                    [140.825091356, 41.794344176],
                    [140.824419186, 41.79364682],
                    [140.82427548, 41.79350203],
                    [140.824200031, 41.793433912],
                    [140.824150639, 41.793393477],
                    [140.824099131, 41.793354557],
                    [140.824045579, 41.793317214],
                    [140.824017504, 41.793299148],
                    [140.823990069, 41.793281502],
                    [140.823932709, 41.793247482],
                    [140.82387356, 41.793215209],
                    [140.823812742, 41.793184728],
                    [140.823750353, 41.79315609],
                    [140.823646666, 41.793113577],
                    [140.823631903, 41.793108266],
                    [140.823514931, 41.793235603],
                    [140.823355755, 41.793177339],
                    [140.822862078, 41.793265333],
                    [140.822882826, 41.793496962],
                ]
            ]
        ]
        c5 = [
            [
                [
                    [143.388539387, 42.903430883],
                    [143.388552596, 42.902885964],
                    [143.387577042, 42.902674614],
                    [143.387558016, 42.902821985],
                    [143.387887082, 42.902951912],
                    [143.387932258, 42.903156554],
                    [143.38815071, 42.903234702],
                    [143.388399847, 42.90358211],
                    [143.388442106, 42.903547921],
                    [143.388420505, 42.903531176],
                    [143.388539387, 42.903430883],
                ]
            ]
        ]
        pd.options.display.float_format = "{:.2f}".format
        return pd.DataFrame(
            {
                "address": ["函館市西旭岡町１丁目44-3", "中川郡幕別町字明野393-8"],
                "座標系": ["公共座標11系", "公共座標13系"],
                "市区町村コード": ["1202", "1643"],
                "coordinates": [c4, c5],
                "面積正解": [3463.7, 3632.1],
            }
        )


class LandsFactory(object):
    @staticmethod
    def build_registration_map():
        raw_csv_path = "tests/management/data/data_models_registrationmap.csv"
        df = pd.read_csv(raw_csv_path)
        return [
            RegistrationMap.objects.create(
                id=params.id,
                geometry=params.geometry,
                coordinate_type=params.coordinate_type,
                area=params.area,
                latitude=params.latitude,
                longitude=params.longitude,
            )
            for _, params in df.iterrows()
        ]

    @staticmethod
    def build_lands():
        raw_csv_path = "tests/management/data/data_models_land.csv"
        df = pd.read_csv(raw_csv_path)
        dataset = []
        for _, params in df.iterrows():
            try:
                land = Land.objects.create(
                    id=params.id,
                    location=params.location,
                    chiban=params.chiban,
                    prefecture_city=PrefecturesCity.objects.filter(
                        id=params.prefecture_city_id
                    ).get(),
                    real_estate_id=params.real_estate_id,
                    latitude=params.latitude,
                    longitude=params.longitude,
                    registration_map=RegistrationMap.objects.filter(
                        id=params.registration_map_id
                    ).get(),
                    owner_latest_get_date=None,
                )
                dataset.append(land)
            except RegistrationMap.DoesNotExist:
                continue
        return dataset
