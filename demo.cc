#include <cassert>
#include <cmath>
#include <cstdio>
#include <ctime>
#include <iostream>
#include <string>

#include "rocksdb/db.h"
#include "rocksdb/options.h"
#include "rocksdb/slice.h"

using namespace std;
using namespace rocksdb;

const std::string PATH = "/tmp/rocksdb_tmp";

const long long limit = 1e18;
const int N = 3e7;
long long get_random() {
  long long rd = rand();
  long long rd2 = rand();
  return (rd << 31ll | rd2) % limit + 1;
  // return rand() % 1000000;
}
int main() {
  freopen("out.txt", "w", stdout);
  clock_t start, end;  //定义clock_t变量
  start = clock();     //开始时间
  DB* db;
  Options options;
  options.write_buffer_size = 4194304;

  options.create_if_missing = true;
  // options.max_bytes_for_level_base=10485760;
  options.max_bytes_for_level_base=1048;

  options.level0_stop_writes_trigger=12;
  options.level0_slowdown_writes_trigger=8;
  options.level0_file_num_compaction_trigger=4;
  options.max_write_buffer_number=1;
  options.max_open_files=1000;

  Status status = DB::Open(options, PATH, &db);
  assert(status.ok());
  for (int i = 0; i < N; i++) {
    std::string key = std::to_string(get_random());
    std::string value = std::to_string(get_random());
    status = db->Put(WriteOptions(), key, value);
    std::string get_value;
    if (status.ok()) {
      status = db->Get(ReadOptions(), key, &get_value);
      if (status.ok()) {
         //printf("get %s\n", get_value.c_str());
      } else {
        printf("get failed\n");
      }
    } else {
      printf("put failed\n");
    }
  }

  delete db;
  end = clock();  //结束时间
  cout << "time = " << double(end - start) / CLOCKS_PER_SEC << "s"
       << endl;  //输出时间
  return 0;
}
