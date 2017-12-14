package com.ds;

public class Array001 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int arr[] = {1, 2, 3, 4, 5, 6, 7};
		int n = 7;
		int d = 4;
		
		//TODO 
		for( int i = 0; i<d; i++){
			int tmp = arr[0];
			for (int j = 0; j < n-1; j++) {
				arr[j] = arr[j+1];
			}
			arr[n-1] = tmp;
		}
		
		
		for( int i = 0; i < 7; i++)
			System.out.println(arr[i]);

	}

}
