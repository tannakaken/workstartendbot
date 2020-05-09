FROM lambci/lambda:build-python3.7
ENV AWS_DEFAULT_REGION ap-northease-1

ADD . .

CMD pip install -r requirements.txt -t /var/task && \
      zip -9 deploy_package.zip lambda_function.py && \
      zip -r9 deploy_package.zip *
