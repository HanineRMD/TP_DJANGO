import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Tutorial } from '../models/tutorial.model';
import { catchError } from 'rxjs/operators';
import { of } from 'rxjs';

const baseUrl = 'https://hanine.pythonanywhere.com/api/tutorials'; // Corrected base URL
const baseUrl1 = 'https://hanine.pythonanywhere.com/api/tutorials/'; // Corrected base URL for operations like POST, DELETE

@Injectable({
  providedIn: 'root'
})
export class TutorialService {

  constructor(private http: HttpClient) { }

  // Get all tutorials
  getAll(): Observable<Tutorial[]> {
    return this.http.get<Tutorial[]>(baseUrl).pipe(
      catchError(error => {
        console.error('Error fetching tutorials:', error);
        return of([]);  // Return an empty array on error
      })
    );
  }

  // Get a specific tutorial by ID
  get(id: any): Observable<Tutorial> {
    return this.http.get<Tutorial>(`${baseUrl1}${id}`).pipe(
      catchError(error => {
        console.error('Error fetching tutorial:', error);
        return of(null);  // Return null on error
      })
    );
  }

  // Create a new tutorial
  create(data: any): Observable<any> {
    return this.http.post(baseUrl1, data).pipe(
      catchError(error => {
        console.error('Error creating tutorial:', error);
        return of(null);  // Return null on error
      })
    );
  }

  // Update an existing tutorial by ID
  update(id: any, data: any): Observable<any> {
    return this.http.put(`${baseUrl1}${id}/`, data).pipe(
      catchError(error => {
        console.error('Error updating tutorial:', error);
        return of(null);  // Return null on error
      })
    );
  }

  // Delete a specific tutorial by ID
  delete(id?: any): Observable<any> {
    const url = id ? `${baseUrl1}${id}/` : baseUrl1;  // If ID is present, delete specific tutorial, else delete all
    return this.http.delete(url).pipe(
      catchError(error => {
        console.error('Error deleting tutorial:', error);
        return of(null);  // Return null on error
      })
    );
  }

  // Delete all tutorials
  deleteAll(): Observable<any> {
    return this.http.delete(baseUrl1).pipe(
      catchError(error => {
        console.error('Error deleting all tutorials:', error);
        return of(null);  // Return null on error
      })
    );
  }

  // Find tutorials by title
  findByTitle(title: any): Observable<Tutorial[]> {
    return this.http.get<Tutorial[]>(`${baseUrl}?title=${title}`).pipe(
      catchError(error => {
        console.error('Error finding tutorials by title:', error);
        return of([]);  // Return an empty array on error
      })
    );
  }
}
