//����ֱ������

typedef struct TMPicture_t{

	unsigned char *data[8];

	int linesize[8];

} TMPicture;

typedef struct TMFrame_t{

	TMPicture pic;//����������

	char* data; //ָ����Ƶ�������ݶε�ָ��

	int len; //��Ƶ�������ݳ���

	int decoded; //�Ƿ��Ѿ�����

	int error;

}TMFrame;

typedef int (*TMReceiverCB)(TMFrame* pFrame, void* arg);//�������ݴ���ص�����ԭ��

typedef enum{

	STORAGE_FT_MP4,

	STORAGE_FT_TS,

	STORAGE_FT_FLV,

	STORAGE_FT_UNKNOWN

}TMStorageFileType;