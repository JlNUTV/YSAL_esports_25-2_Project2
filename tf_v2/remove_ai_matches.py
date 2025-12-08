import pandas as pd

# high_ai_matches.csv에서 filename 목록 읽기
high_ai_df = pd.read_csv('high_ai_matches.csv')
ai_filenames = set(high_ai_df['filename'].values)

print(f"제거할 AI 매치 수: {len(ai_filenames)}")

# data_v2.csv 읽기
print("data_v2.csv 읽는 중...")
data_df = pd.read_csv('data_v2.csv')
original_count = len(data_df)
print(f"원본 데이터 행 수: {original_count}")

# match_id가 ai_filenames에 없는 행만 유지
filtered_df = data_df[~data_df['match_id'].isin(ai_filenames)]
filtered_count = len(filtered_df)
removed_count = original_count - filtered_count

print(f"필터링 후 데이터 행 수: {filtered_count}")
print(f"제거된 행 수: {removed_count}")

# 결과 저장
output_file = 'data_v2_filtered.csv'
filtered_df.to_csv(output_file, index=False)
print(f"\n결과가 '{output_file}'에 저장되었습니다.")
