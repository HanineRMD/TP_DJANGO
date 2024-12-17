import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Tutorial } from '../models/tutorial.model';

const baseUrl = 'http://localhost:8000/api/tutorials';
const baseUrl1 = 'http://localhost:8000/api/tutorials/';


@Injectable({
  providedIn: 'root'
})
export class TutorialService {

  constructor(private http: HttpClient) { }

  getAll(): Observable<Tutorial[]> {
    return this.http.get<Tutorial[]>(baseUrl);
  }

  get(id: any): Observable<Tutorial> {
    return this.http.get<Tutorial>(`${baseUrl}/${id}`);
  }

  create(data: any): Observable<any> {
    return this.http.post(baseUrl1, data);
  }

  update(id: any, data: any): Observable<any> {
    return this.http.put(`${baseUrl}/${id}/`, data);
  }
  
  delete(id: any): Observable<any> {
    // Ensure that the ID is not undefined or null before constructing the URL
    const url = id ? `${baseUrl1}${id}/` : baseUrl1;  // If id is present, add it to the URL, otherwise use baseUrl1 (for deleteAll)
    return this.http.delete(url);
  }
  

  deleteAll(): Observable<any> {
    return this.http.delete(baseUrl1);
  }

  findByTitle(title: any): Observable<Tutorial[]> {
    return this.http.get<Tutorial[]>(`${baseUrl}?title=${title}`);
  }
}