# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.pipelines.files import FilesPipeline
import urllib.parse
import logging
import scrapy


logger = logging.getLogger(__name__)

class CustomFilePipeline(FilesPipeline) :


    def __parseFileName(self, url) :
        params = urllib.parse.parse_qs(urllib.parse.urlparse(url).query) 
        return params['attname'][0]

    def get_media_requests(self, items, info) :
        for fileUrl in items['file_urls'] :
            logger.info('download file %s', self.__parseFileName(fileUrl))
            yield scrapy.Request(fileUrl, meta={'subdir': items['sub_dir']})

    def file_path(self, request, response=None, info=None) :
        try :
            fileName = self.__parseFileName(request.url)
            subDir = request.meta['subdir']
            return "/".join([subDir, fileName])
        except Exception as exc:
            logger.error("error %s", str(exc))