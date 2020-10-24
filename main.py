from download_resource_images import download_resource_images
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

url_list = [
    "https://www.saizeriya.co.jp/entertainment/images/1710/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1801/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1804/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1806/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1810/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1812/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1904/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1907/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1910/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/1912/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/2003/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/2007/body.png",
    "https://www.saizeriya.co.jp/entertainment/images/2009/body.png"
]
resource_path = "resource"
intermediate_path = "intermediate"
result_path = "result"

# 間違い探しのオリジナル画像をサイゼリヤのWebサイトからダウンロード
download_resource_images(url_list, resource_path)

# 以下はまだ1ケースのみの実装(後で全ケースの再帰的な実行へリファクタリング予定)

# 間違い探しの画像領域の特定(グレースケール化→二値化→輪郭検出→左右分割領域検出)
convert_color_image_file_to_bw_image_file_with_manual_threshold(
    "resource/1710/saizeriya_photo_hunt_original_image.png",
    "intermediate/1710/010_saizeriya_photo_hunt_detect_field_image.png",
    254
)
detect_field_x = detect_field_image_x_range(
    "intermediate/1710/010_saizeriya_photo_hunt_detect_field_image.png"
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
    "resource/1710/saizeriya_photo_hunt_original_image.png",
    "intermediate/1710/020_saizeriya_photo_hunt_left_image.png",
    left_image_x_min,
    left_image_x_max,
    left_image_y_min,
    left_image_y_max
)

# 間違い探しの画像の右側の画像を切り抜き
crop_image(
    "resource/1710/saizeriya_photo_hunt_original_image.png",
    "intermediate/1710/030_saizeriya_photo_hunt_right_image.png",
    right_image_x_min,
    right_image_x_max,
    right_image_y_min,
    right_image_y_max
)

# サイズが全く同じ左右画像の差分画像を取得...平行移動のため使い物にならないくらい無駄に差分検出されている
create_diff_image_file(
    "intermediate/1710/020_saizeriya_photo_hunt_left_image.png",
    "intermediate/1710/030_saizeriya_photo_hunt_right_image.png",
    "intermediate/1710/040_saizeriya_photo_hunt_diff_image.png"
)

# 左右画像内の特徴点のマッチングで平行移動量を推定
translation_vector = feature_point_matching(
    "intermediate/1710/020_saizeriya_photo_hunt_left_image.png",
    "intermediate/1710/030_saizeriya_photo_hunt_right_image.png",
    "intermediate/1710/050_saizeriya_photo_hunt_matching_result_image.png"
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
    "resource/1710/saizeriya_photo_hunt_original_image.png",
    "intermediate/1710/060_saizeriya_photo_hunt_modified_left_image.png",
    left_image_x_min,
    left_image_x_max,
    left_image_y_min,
    left_image_y_max
)

# 間違い探しの画像の右側の画像を切り抜き(平行移動量推定を反映)
crop_image(
    "resource/1710/saizeriya_photo_hunt_original_image.png",
    "intermediate/1710/070_saizeriya_photo_hunt_modified_right_image.png",
    right_image_x_min,
    right_image_x_max,
    right_image_y_min,
    right_image_y_max
)

# サイズが全く同じ左右画像の差分画像を取得...平行移動補正済
create_diff_image_file(
    "intermediate/1710/060_saizeriya_photo_hunt_modified_left_image.png",
    "intermediate/1710/070_saizeriya_photo_hunt_modified_right_image.png",
    "intermediate/1710/080_saizeriya_photo_hunt_modified_diff_image.png"
)

# 差分画像を白黒化
convert_color_image_file_to_bw_image_file(
    "intermediate/1710/080_saizeriya_photo_hunt_modified_diff_image.png",
    "intermediate/1710/090_saizeriya_photo_hunt_modified_bw_diff_image.png"
)

# 平行移動の誤差を除去するため、白黒化した差分画像をモルフォロジー変換で収縮
erose_bw_image_file(
    "intermediate/1710/090_saizeriya_photo_hunt_modified_bw_diff_image.png",
    "intermediate/1710/100_saizeriya_photo_hunt_modified_bw_diff_mask_image_with_noise.png",
    1,
    3,
    2
)

# 残ったわずかなノイズをモルフォロジー変換のオープニング処理で除去
denoise_bw_image_file(
    "intermediate/1710/100_saizeriya_photo_hunt_modified_bw_diff_mask_image_with_noise.png",
    "intermediate/1710/110_saizeriya_photo_hunt_modified_bw_diff_mask_image.png",
    2,
    2
)

# 誤差・ノイズ除去のため検出領域が狭くなりすぎているのをモルフォロジー変換で膨張
dilate_bw_image_file(
    "intermediate/1710/110_saizeriya_photo_hunt_modified_bw_diff_mask_image.png",
    "intermediate/1710/120_saizeriya_photo_hunt_modified_bw_diff_mask_image_result.png",
    2,
    2,
    10
)


# 間違い箇所のみ切り抜いた結果画像を作成
create_result_image_file(
    "intermediate/1710/080_saizeriya_photo_hunt_modified_diff_image.png",
    "intermediate/1710/120_saizeriya_photo_hunt_modified_bw_diff_mask_image_result.png",
    "result/1710/saizeriya_photo_hunt_result_image.png",
    "intermediate/1710/060_saizeriya_photo_hunt_modified_left_image.png",
    "intermediate/1710/070_saizeriya_photo_hunt_modified_right_image.png"
)
