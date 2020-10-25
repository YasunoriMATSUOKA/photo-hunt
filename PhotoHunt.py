from download_file import download_file
from convert_color_image_file_to_bw_image_file_with_manual_threshold import convert_color_image_file_to_bw_image_file_with_manual_threshold
from detect_field_image_x_range import detect_field_image_x_range
from crop_image import crop_image
from create_diff_image_file import create_diff_image_file
from feature_point_matching import feature_point_matching
from convert_color_image_file_to_bw_image_file import convert_color_image_file_to_bw_image_file
from erose_bw_image_file import erose_bw_image_file
from denoise_bw_image_file import denoise_bw_image_file
from dilate_bw_image_file import dilate_bw_image_file
from create_result_image_file import create_result_image_file

saizeriya_photo_base_url = "https://www.saizeriya.co.jp/entertainment/images"
saizeriya_photo_base_file_name = "body.png"

resource_dir = "resource"
intermediate_dir = "intermediate"
result_dir = "result"

resource_original_image_file_name = "original_image.png"

intermediate_detect_field_image_file_name = "010_detect_field_image.png"
intermediate_left_image_file_name = "020_left_image.png"
intermediate_right_image_file_name = "030_right_image.png"
intermediate_diff_image_file_name = "040_diff_image.png"
intermediate_matching_result_image_file_name = "050_matching_result_image.png"
intermediate_modified_left_image_file_name = "060_modified_left_image.png"
intermediate_modified_right_image_file_name = "070_modified_right_image.png"
intermediate_modified_diff_image_file_name = "080_modified_diff_image.png"
intermediate_modified_bw_diff_image_file_name = "090_modified_bw_diff_image.png"
intermediate_modified_bw_diff_mask_with_noise_image_file_name = "100_modified_bw_diff_mask_with_noise_image.png"
intermediate_modified_bw_diff_mask_image_file_name = "110_modified_bw_diff_mask_image.png"
intermediate_modified_bw_diff_mask_result_image_file_name = "120_modified_bw_diff_mask_result_image.png"
intermediate_result_with_mask_image_file_name = "130_result_with_mask_image.png"

result_image_file_name = "result_image.png"


class PhotoHunt:
    url = ""
    resource_original_image_file_path = ""
    intermediate_detect_field_image_file_path = ""
    intermediate_left_image_file_path = ""
    intermediate_right_image_file_path = ""
    intermediate_diff_image_file_path = ""
    intermediate_matching_result_image_file_path = ""
    intermediate_modified_left_image_file_path = ""
    intermediate_modified_right_image_file_path = ""
    intermediate_modified_diff_image_file_path = ""
    intermediate_modified_bw_diff_image_file_path = ""
    intermediate_modified_bw_diff_mask_with_noise_image_file_path = ""
    intermediate_modified_bw_diff_mask_image_file_path = ""
    intermediate_modified_bw_diff_mask_result_image_file_path = ""
    intermediate_result_with_mask_image_file_path = ""
    result_image_file_path = ""

    def __init__(self, url):
        self.url = url
        self.resource_original_image_file_path = self.convert_url_to_file_path(
            resource_dir,
            resource_original_image_file_name
        )
        self.intermediate_detect_field_image_file_path = self.convert_url_to_file_path(
            intermediate_dir,
            intermediate_detect_field_image_file_name
        )
        self.intermediate_left_image_file_path = self.convert_url_to_file_path(
            intermediate_dir,
            intermediate_left_image_file_name
        )
        self.intermediate_right_image_file_path = self.convert_url_to_file_path(
            intermediate_dir,
            intermediate_right_image_file_name
        )
        self.intermediate_diff_image_file_path = self.convert_url_to_file_path(
            intermediate_dir,
            intermediate_diff_image_file_name
        )
        self.intermediate_matching_result_image_file_path = self.convert_url_to_file_path(
            intermediate_dir,
            intermediate_matching_result_image_file_name
        )
        self.intermediate_modified_left_image_file_path = self.convert_url_to_file_path(
            intermediate_dir,
            intermediate_modified_left_image_file_name
        )
        self.intermediate_modified_right_image_file_path = self.convert_url_to_file_path(
            intermediate_dir,
            intermediate_modified_right_image_file_name
        )
        self.intermediate_modified_diff_image_file_path = self.convert_url_to_file_path(
            intermediate_dir,
            intermediate_modified_diff_image_file_name
        )
        self.intermediate_modified_bw_diff_image_file_path = self.convert_url_to_file_path(
            intermediate_dir,
            intermediate_modified_bw_diff_image_file_name
        )
        self.intermediate_modified_bw_diff_mask_with_noise_image_file_path = self.convert_url_to_file_path(
            intermediate_dir,
            intermediate_modified_bw_diff_mask_with_noise_image_file_name
        )
        self.intermediate_modified_bw_diff_mask_image_file_path = self.convert_url_to_file_path(
            intermediate_dir,
            intermediate_modified_bw_diff_mask_image_file_name
        )
        self.intermediate_modified_bw_diff_mask_result_image_file_path = self.convert_url_to_file_path(
            intermediate_dir,
            intermediate_modified_bw_diff_mask_result_image_file_name
        )
        self.intermediate_result_with_mask_image_file_path = self.convert_url_to_file_path(
            intermediate_dir,
            intermediate_result_with_mask_image_file_name
        )
        self.result_image_file_path = self.convert_url_to_file_path(
            result_dir,
            result_image_file_name
        )

        print(self.url)
        print(self.resource_original_image_file_path)
        print(self.intermediate_detect_field_image_file_path)
        print(self.intermediate_left_image_file_path)
        print(self.intermediate_right_image_file_path)
        print(self.intermediate_diff_image_file_path)
        print(self.intermediate_matching_result_image_file_path)
        print(self.intermediate_modified_left_image_file_path)
        print(self.intermediate_modified_right_image_file_path)
        print(self.intermediate_modified_diff_image_file_path)
        print(self.intermediate_modified_bw_diff_image_file_path)
        print(self.intermediate_modified_bw_diff_mask_with_noise_image_file_path)
        print(self.intermediate_modified_bw_diff_mask_image_file_path)
        print(self.intermediate_modified_bw_diff_mask_result_image_file_path)
        print(self.intermediate_result_with_mask_image_file_path)
        print(self.result_image_file_path)

    def convert_url_to_file_path(self, target_dir, file_name):
        path = self.url.replace(
            saizeriya_photo_base_url,
            target_dir
        ).replace(
            saizeriya_photo_base_file_name,
            file_name
        )
        return path

    def execute(self):
        # 間違い探しのオリジナル画像をサイゼリヤのWebサイトからダウンロード
        download_file(
            self.url,
            self.resource_original_image_file_path
        )

        # 間違い探しの画像領域の特定(グレースケール化→二値化→輪郭検出→左右分割領域検出)
        convert_color_image_file_to_bw_image_file_with_manual_threshold(
            self.resource_original_image_file_path,
            self.intermediate_detect_field_image_file_path,
            254
        )
        detect_field_x = detect_field_image_x_range(
            self.intermediate_detect_field_image_file_path
        )

        left_image_x_min = detect_field_x[0]
        left_image_x_max = detect_field_x[1]
        left_image_y_min = detect_field_x[2]
        left_image_y_max = detect_field_x[3]
        right_image_x_min = detect_field_x[4]
        right_image_x_max = detect_field_x[5]
        right_image_y_min = detect_field_x[6]
        right_image_y_max = detect_field_x[7]

        left_image_size = detect_field_x[8]
        right_image_size = detect_field_x[9]

        # 間違い探しの画像の左側の画像を切り抜き
        crop_image(
            self.resource_original_image_file_path,
            self.intermediate_left_image_file_path,
            left_image_x_min,
            left_image_x_max,
            left_image_y_min,
            left_image_y_max
        )

        # 間違い探しの画像の右側の画像を切り抜き
        crop_image(
            self.resource_original_image_file_path,
            self.intermediate_right_image_file_path,
            right_image_x_min,
            right_image_x_max,
            right_image_y_min,
            right_image_y_max
        )

        # サイズが全く同じ左右画像の差分画像を取得...平行移動のため使い物にならないくらい無駄に差分検出されている
        create_diff_image_file(
            self.intermediate_left_image_file_path,
            self.intermediate_right_image_file_path,
            self.intermediate_diff_image_file_path
        )

        # 左右画像内の特徴点のマッチングで平行移動量を推定
        translation_vector = feature_point_matching(
            self.intermediate_left_image_file_path,
            self.intermediate_right_image_file_path,
            self.intermediate_matching_result_image_file_path
        )

        # 推定した平行移動量に基づいてクロップ領域を修正
        translation_vector_x = translation_vector[0]
        translation_vector_y = translation_vector[1]
        if translation_vector_x < 0:
            left_image_x_min = left_image_x_min - translation_vector_x
            right_image_x_max = right_image_x_max + translation_vector_x
        elif translation_vector_x > 0:
            left_image_x_min = left_image_x_min + translation_vector_x
            right_image_x_max = right_image_x_max - translation_vector_x

        # 間違い探しの画像の左側の画像を切り抜き(平行移動量推定を反映)
        crop_image(
            self.resource_original_image_file_path,
            self.intermediate_modified_left_image_file_path,
            left_image_x_min,
            left_image_x_max,
            left_image_y_min,
            left_image_y_max
        )

        # 間違い探しの画像の右側の画像を切り抜き(平行移動量推定を反映)
        crop_image(
            self.resource_original_image_file_path,
            self.intermediate_modified_right_image_file_path,
            right_image_x_min,
            right_image_x_max,
            right_image_y_min,
            right_image_y_max
        )

        # サイズが全く同じ左右画像の差分画像を取得...平行移動補正済
        create_diff_image_file(
            self.intermediate_modified_left_image_file_path,
            self.intermediate_modified_right_image_file_path,
            self.intermediate_modified_diff_image_file_path
        )

        # 差分画像を白黒化
        convert_color_image_file_to_bw_image_file(
            self.intermediate_modified_diff_image_file_path,
            self.intermediate_modified_bw_diff_image_file_path
        )

        # 平行移動の誤差を除去するため、白黒化した差分画像をモルフォロジー変換で収縮
        erose_bw_image_file(
            self.intermediate_modified_bw_diff_image_file_path,
            self.intermediate_modified_bw_diff_mask_with_noise_image_file_path,
            1,
            3,
            2
        )

        # 残ったわずかなノイズをモルフォロジー変換のオープニング処理で除去
        denoise_bw_image_file(
            self.intermediate_modified_bw_diff_mask_with_noise_image_file_path,
            self.intermediate_modified_bw_diff_mask_image_file_path,
            2,
            2
        )

        # 誤差・ノイズ除去のため検出領域が狭くなりすぎているのをモルフォロジー変換で膨張
        dilate_bw_image_file(
            self.intermediate_modified_bw_diff_mask_image_file_path,
            self.intermediate_modified_bw_diff_mask_result_image_file_path,
            2,
            2,
            10
        )

        # 間違い箇所のみ切り抜いた結果画像を作成
        create_result_image_file(
            self.intermediate_modified_diff_image_file_path,
            self.intermediate_modified_bw_diff_mask_result_image_file_path,
            self.intermediate_result_with_mask_image_file_path,
            self.result_image_file_path,
            self.intermediate_modified_left_image_file_path,
            self.intermediate_modified_right_image_file_path
        )
