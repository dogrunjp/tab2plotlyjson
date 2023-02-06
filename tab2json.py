# -*- encoding: utf-8 -*-
import csv, json


def metagenomic_composition(input_f: str, samples:list) -> list:
    """
    系統組成データをcsvから取得する
    :param input_f:
    :return: ヘッダ付きのtaxonごとのリード数データセット
    """
    csv_file = open(input_f,  "r", encoding="ms932")
    #reader = csv.reader(csv_file, delimiter="\t")
    reader = csv.DictReader(csv_file, delimiter="\t")
    tbl = [r for r in reader]
    # ２階層のリストで１階層目がサンプル名、２行目移行[taxon, value1, value1,,,]というデータ
    # print(tbl[0]["HWVHNDSXX_PG3460_569A9595"])
    # 選択したサンプルのリスト作成
    # taxごとに選択したサンプルの情報の値をマップする
    res_plotly = []

    for t in tbl:
        """
        taxonごと繰り返す
        """
        taxon = next(iter(t.items()))[1]
        # サンプルごとの処理
        vals = map(lambda x: {"x":samples,"y":t[x], "name":x, "type":"bar"},  samples)
        y = []
        for s in samples:
            """
            サンプルごとにリード数を取得しy:listにappendする
            """
            y.append(t[s])
        obj = {"x":samples, "y": y, "name": taxon, "type": "bar"}
        res_plotly.append(obj)

    return res_plotly


def plotly_json(input_f: str, output_f:str, samples:list):
    d = metagenomic_composition(input_f, samples)
    with open(output_f, "w") as f:
        json.dump(d, f, indent=4)


if __name__ == "__main__":
    samples = ["H53G2DSXY_PG3460_759A5454", "H53G2DSXY_PG3460_761A5757", "H53G2DSXY_PG3460_767A6363"]
    plotly_json("/Users/oec/Desktop/data/MDB/系統組成データ_plotly用_20230205/1269SampleGenusMajor.txt", "test_plotly.json", samples)
